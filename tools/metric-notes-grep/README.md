# metric-notes-grep

Локальный MCP-сервер для поиска по Markdown-базе знаний проекта без RAG, embeddings и vector DB.

## Что делает

Даёт агенту два инструмента:

- **`grep_notes`** — literal substring поиск по `.md` файлам. Возвращает совпадения с
  относительным путём (POSIX), номером строки и сниппетом контекста.
- **`read_note`** — чтение фрагмента файла по относительному пути из `NOTES_ROOT`.

Никакого regex. Никакой индексации. Никакого кэша. Просто `os.walk` + `needle in haystack`.

## Установка (с нуля, Windows)

Из корня проекта:

```powershell
# 1. Создать venv (используем системный Python 3.11+)
python -m venv tools\metric-notes-grep\.venv

# 2. Установить зависимости
& "tools\metric-notes-grep\.venv\Scripts\python.exe" -m pip install --upgrade pip
& "tools\metric-notes-grep\.venv\Scripts\python.exe" -m pip install "mcp[cli]>=1.0,<2.0"
```

## Регистрация

В плагине сервер уже подключён через `.mcp.json` в корне репозитория:

```json
"metric-notes-grep": {
  "type": "stdio",
  "command": "python",
  "args": ["tools/metric-notes-grep/server.py"],
  "env": { "NOTES_ROOT": "." }
}
```

Для ручного подключения в другом окружении (venv из раздела «Установка», пути относительно корня репозитория):

```json
"metric-notes-grep": {
  "type": "stdio",
  "command": "tools/metric-notes-grep/.venv/Scripts/python.exe",
  "args": ["tools/metric-notes-grep/server.py"],
  "env": { "NOTES_ROOT": "." }
}
```

После правки конфига — перезапустить клиент (Claude Code / Kilo).

## Переменные окружения

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `NOTES_ROOT` | `cwd` сервера | Корень базы знаний |
| `INCLUDE_EXTENSIONS` | `.md` | CSV-список расширений (например `.md,.txt`) |
| `EXCLUDE_DIRS` | см. ниже | CSV относительных папок для исключения |
| `MAX_FILE_SIZE_KB` | `2048` | Не открывать файлы крупнее |

**Дефолтные `EXCLUDE_DIRS`:**

```
.kilo/node_modules, .obsidian, .git,
node_modules, .venv, tools/metric-notes-grep/.venv, __pycache__
```

## API инструментов

### `grep_notes`

| Параметр | Тип | По умолчанию | Описание |
| --- | --- | --- | --- |
| `query` | string | — (required) | Подстрока (literal). |
| `limit` | int | `20` | Максимум совпадений. |
| `context_lines` | int | `2` | Строк до/после совпадения в сниппете. |
| `case_sensitive` | bool | `false` | Регистрозависимость. |
| `path_filter` | string? | `null` | Glob по relative_path в POSIX (`METHODOLOGY/**`). |

Возвращает:

```json
{
  "matches": [
    {
      "relative_path": "METHODOLOGY/index/glossary.md",
      "line_number": 14,
      "match_line": "| **CAC** | ...",
      "snippet": "13: ...\n14: ...\n15: ..."
    }
  ],
  "returned_count": 1,
  "truncated": false
}
```

- `relative_path` — всегда POSIX (`/`).
- `returned_count` — длина массива `matches`.
- `truncated = true`, если поиск остановлен по `limit` (совпадений в базе больше).

### `read_note`

| Параметр | Тип | По умолчанию | Описание |
| --- | --- | --- | --- |
| `relative_path` | string | — (required) | Путь из `NOTES_ROOT` (POSIX или Windows). |
| `start_line` | int | `1` | Стартовая строка (1-indexed). |
| `end_line` | int? | `null` | Конечная строка включительно. |
| `max_lines` | int | `400` | Жёсткий лимит на размер ответа. |

Возвращает:

```json
{
  "relative_path": "METHODOLOGY/index/glossary.md",
  "start_line": 1,
  "end_line": 30,
  "total_lines": 34,
  "content": "1: # Глоссарий\n2: ..."
}
```

Защита от path traversal: путь резолвится и проверяется, что он внутри `NOTES_ROOT`,
иначе возвращается `{"error": "PathOutsideRoot: ..."}`.

## Smoke-тесты

После подключения MCP — спросите агента:

1. `grep_notes("NSM", limit=5)` — должен найти строки в `METHODOLOGY/index/glossary.md`,
   `heuristics.md`, `skills/metrics-pyramid/SKILL.md`.
2. `grep_notes("Правила ревьюера")` — 1+ совпадение в `METHODOLOGY/index/heuristics.md`.
3. `grep_notes("Retention", path_filter="METHODOLOGY/**")` — совпадения в `METHODOLOGY/index/`.
4. `grep_notes("anything", path_filter="EVALS/**")` — только из `EVALS/`.
5. `read_note("METHODOLOGY/index/glossary.md", 1, 30)` — фрагмент с префиксами `N: `.
6. `read_note("../../../etc/passwd")` — ошибка `PathOutsideRoot`.
