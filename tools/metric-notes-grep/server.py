"""metric-notes-grep — локальный MCP-сервер для поиска по Markdown-базе знаний.

Два инструмента:
  - grep_notes : literal substring search по .md файлам
  - read_note  : чтение фрагмента файла по относительному пути (POSIX)

Принципы v1:
  - Никакого regex / re. Только `needle in haystack`.
  - Все relative_path нормализованы к POSIX (forward slashes).
  - Защита от path traversal: read_note валидирует, что путь внутри NOTES_ROOT.

Конфигурация через переменные окружения:
  NOTES_ROOT          — корень базы знаний (default: cwd)
  INCLUDE_EXTENSIONS  — CSV расширений (default: ".md")
  EXCLUDE_DIRS        — CSV относительных папок (default: см. DEFAULT_EXCLUDE_DIRS)
  MAX_FILE_SIZE_KB    — лимит размера файла (default: 2048)
"""

from __future__ import annotations

import os
from fnmatch import fnmatch
from pathlib import Path, PurePosixPath
from typing import Any

from mcp.server.fastmcp import FastMCP


# ---------- Конфигурация ----------

DEFAULT_EXCLUDE_DIRS = [
    ".kilo/node_modules",
    ".obsidian",
    ".git",
    "node_modules",
    ".venv",
    "tools/metric-notes-grep/.venv",
    "__pycache__",
]


def _csv_env(name: str, default: list[str]) -> list[str]:
    raw = os.environ.get(name)
    if not raw:
        return list(default)
    return [item.strip() for item in raw.split(",") if item.strip()]


NOTES_ROOT = Path(os.environ.get("NOTES_ROOT", os.getcwd())).resolve()
INCLUDE_EXTENSIONS = {
    ext.lower() if ext.startswith(".") else f".{ext.lower()}"
    for ext in _csv_env("INCLUDE_EXTENSIONS", [".md"])
}
EXCLUDE_DIRS_POSIX = {
    PurePosixPath(p.replace("\\", "/")).as_posix()
    for p in _csv_env("EXCLUDE_DIRS", DEFAULT_EXCLUDE_DIRS)
}
MAX_FILE_SIZE_BYTES = int(os.environ.get("MAX_FILE_SIZE_KB", "2048")) * 1024


# ---------- Утилиты ----------

def _to_posix(rel_path: Path) -> str:
    """Превратить относительный путь в POSIX-вид (forward slashes)."""
    return PurePosixPath(rel_path.as_posix()).as_posix()


def _normalize_filter(pattern: str) -> str:
    """Нормализовать path_filter к POSIX-виду для fnmatch."""
    return pattern.replace("\\", "/")


def _is_excluded(rel_dir_posix: str) -> bool:
    """Проверить, попадает ли каталог в exclude-список (по префиксу пути)."""
    if rel_dir_posix in EXCLUDE_DIRS_POSIX:
        return True
    for excl in EXCLUDE_DIRS_POSIX:
        if rel_dir_posix == excl or rel_dir_posix.startswith(excl + "/"):
            return True
    return False


def _iter_files() -> list[tuple[Path, str]]:
    """Обойти NOTES_ROOT, вернуть [(абс. путь, POSIX относительный путь), ...]."""
    results: list[tuple[Path, str]] = []
    root_str = str(NOTES_ROOT)

    for dirpath, dirnames, filenames in os.walk(root_str):
        current = Path(dirpath)
        try:
            rel_dir = current.relative_to(NOTES_ROOT)
        except ValueError:
            continue
        rel_dir_posix = _to_posix(rel_dir) if str(rel_dir) != "." else ""

        # Отсечь поддеревья на основе текущего относительного пути
        kept = []
        for d in dirnames:
            sub_rel = f"{rel_dir_posix}/{d}" if rel_dir_posix else d
            if not _is_excluded(sub_rel):
                kept.append(d)
        dirnames[:] = sorted(kept)

        # Если сам текущий каталог в исключениях — пропустить файлы
        if rel_dir_posix and _is_excluded(rel_dir_posix):
            continue

        for fname in sorted(filenames):
            ext = Path(fname).suffix.lower()
            if ext not in INCLUDE_EXTENSIONS:
                continue
            abs_path = current / fname
            try:
                if abs_path.stat().st_size > MAX_FILE_SIZE_BYTES:
                    continue
            except OSError:
                continue
            rel_file = abs_path.relative_to(NOTES_ROOT)
            results.append((abs_path, _to_posix(rel_file)))
    return results


def _build_snippet(lines: list[str], idx: int, context: int) -> str:
    """Собрать сниппет с префиксами 'N: ' для строк вокруг idx (0-based)."""
    start = max(0, idx - context)
    end = min(len(lines), idx + context + 1)
    parts = []
    for i in range(start, end):
        # rstrip только \r\n, чтобы не потерять отступы
        text = lines[i].rstrip("\r\n")
        parts.append(f"{i + 1}: {text}")
    return "\n".join(parts)


def _resolve_inside_root(relative_path: str) -> Path:
    """Безопасно превратить relative_path (POSIX или нативный) в абс. путь внутри NOTES_ROOT."""
    cleaned = relative_path.replace("\\", "/").lstrip("/")
    candidate = (NOTES_ROOT / cleaned).resolve()
    try:
        candidate.relative_to(NOTES_ROOT)
    except ValueError as exc:
        raise ValueError(f"PathOutsideRoot: {relative_path}") from exc
    return candidate


# ---------- MCP-сервер ----------

mcp = FastMCP("metric-notes-grep")


@mcp.tool()
def grep_notes(
    query: str,
    limit: int = 20,
    context_lines: int = 2,
    case_sensitive: bool = False,
    path_filter: str | None = None,
) -> dict[str, Any]:
    """Найти literal substring совпадения по Markdown-файлам базы знаний.

    Args:
        query: Подстрока для поиска (literal, без regex).
        limit: Максимум совпадений в ответе.
        context_lines: Сколько строк до/после строки-совпадения.
        case_sensitive: Регистрозависимый ли поиск.
        path_filter: Опциональный glob по относительному пути в POSIX-виде
                     (например, "METHODOLOGY/**" или "SKILLS/**/*.md").

    Returns:
        {
          "matches": [{"relative_path", "line_number", "match_line", "snippet"}, ...],
          "returned_count": <len(matches)>,
          "truncated": <bool — true, если остановились по limit>
        }
    """
    if not isinstance(query, str) or query == "":
        return {"matches": [], "returned_count": 0, "truncated": False,
                "error": "query must be a non-empty string"}
    if limit <= 0:
        limit = 1
    if context_lines < 0:
        context_lines = 0

    needle = query if case_sensitive else query.lower()
    filter_norm = _normalize_filter(path_filter) if path_filter else None

    matches: list[dict[str, Any]] = []

    for abs_path, rel_posix in _iter_files():
        if filter_norm and not fnmatch(rel_posix, filter_norm):
            continue
        try:
            with open(abs_path, encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
        except OSError:
            continue

        for i, line in enumerate(lines):
            haystack = line if case_sensitive else line.lower()
            if needle in haystack:
                matches.append({
                    "relative_path": rel_posix,
                    "line_number": i + 1,
                    "match_line": line.rstrip("\r\n"),
                    "snippet": _build_snippet(lines, i, context_lines),
                })
                if len(matches) >= limit:
                    return {
                        "matches": matches,
                        "returned_count": len(matches),
                        "truncated": True,
                    }

    return {
        "matches": matches,
        "returned_count": len(matches),
        "truncated": False,
    }


@mcp.tool()
def read_note(
    relative_path: str,
    start_line: int = 1,
    end_line: int | None = None,
    max_lines: int = 400,
) -> dict[str, Any]:
    """Прочитать фрагмент Markdown-файла по относительному пути из NOTES_ROOT.

    Args:
        relative_path: Путь относительно NOTES_ROOT (POSIX или Windows; будет нормализован).
        start_line: Стартовая строка (1-indexed).
        end_line: Конечная строка включительно. Если None — до конца файла или до max_lines.
        max_lines: Жёсткий лимит количества строк в ответе.

    Returns:
        {"relative_path", "start_line", "end_line", "total_lines", "content"}
        content — строки с префиксом "N: " (как в grep snippet).
    """
    try:
        abs_path = _resolve_inside_root(relative_path)
    except ValueError as exc:
        return {"error": str(exc)}

    if not abs_path.is_file():
        return {"error": f"NotAFile: {relative_path}"}

    if start_line < 1:
        start_line = 1
    if max_lines <= 0:
        max_lines = 1

    try:
        with open(abs_path, encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
    except OSError as exc:
        return {"error": f"ReadError: {exc}"}

    total = len(lines)
    if start_line > total:
        return {
            "relative_path": _to_posix(abs_path.relative_to(NOTES_ROOT)),
            "start_line": start_line,
            "end_line": start_line - 1,
            "total_lines": total,
            "content": "",
        }

    if end_line is None:
        end_idx = min(total, start_line - 1 + max_lines)
    else:
        end_idx = min(total, end_line, start_line - 1 + max_lines)

    parts = []
    for i in range(start_line - 1, end_idx):
        parts.append(f"{i + 1}: {lines[i].rstrip(chr(10)).rstrip(chr(13))}")

    return {
        "relative_path": _to_posix(abs_path.relative_to(NOTES_ROOT)),
        "start_line": start_line,
        "end_line": end_idx,
        "total_lines": total,
        "content": "\n".join(parts),
    }


if __name__ == "__main__":
    mcp.run()
