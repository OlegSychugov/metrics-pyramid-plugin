---
name: excel
description: Работа с Excel-таблицами — чтение, создание, редактирование и аналитика .xlsx файлов
license: MIT
metadata:
  version: 1.0.0
---

## Обзор

Инструмент для работы с Excel-документами (.xlsx). Работай через Bash: создавай
и запускай python-скрипты в рабочей директории пользователя (openpyxl и pandas
предустановлены или ставятся через pip).

Библиотеки:
- **`openpyxl`** — для создания, точечного редактирования и сохранения
  форматирования
- **`pandas`** — для аналитики, агрегаций, фильтров, чтения больших
  файлов и работы с CSV

## Когда что выбрать

| Задача | Инструмент |
|---|---|
| Создать файл с нуля | `openpyxl` |
| Подставить значение в шаблон, сохранив формат | `openpyxl` |
| Нарисовать таблицу со стилями (жирные шапки, границы) | `openpyxl` |
| Прочитать содержимое и показать пользователю | `pandas` |
| Любая агрегация (сумма, среднее, top-N, group by) | `pandas` |
| Фильтр строк по условию | `pandas` |
| Файл от 10к строк | `pandas` |
| CSV / TSV | `pandas` |
| Объединить два файла/листа по ключу | `pandas` |

## Примеры — openpyxl (создание и точечные правки)

### Создание файла

```python
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Отчёт"
ws.append(["Клиент", "Сумма", "Дата"])
ws.append(["ООО Ромашка", 150000, "2026-04-15"])
ws.append(["ИП Иванов", 75000, "2026-04-20"])
wb.save("report.xlsx")
```

### Несколько листов

```python
import openpyxl
wb = openpyxl.Workbook()
wb.remove(wb.active)
sales = wb.create_sheet("Продажи")
sales.append(["Клиент", "Сумма"])
sales.append(["ООО Ромашка", 150000])
expenses = wb.create_sheet("Расходы")
expenses.append(["Статья", "Сумма"])
expenses.append(["Аренда", 50000])
wb.save("report.xlsx")
```

### Точечное обновление ячейки в шаблоне

Сохраняет всё остальное содержимое, формулы и форматирование:

```python
import openpyxl
wb = openpyxl.load_workbook("template.xlsx")
ws = wb["Отчёт"]
ws["B5"] = 1500000
wb.save("template.xlsx")
```

### Жирные заголовки

```python
import openpyxl
from openpyxl.styles import Font
wb = openpyxl.load_workbook("report.xlsx")
ws = wb.active
for cell in ws[1]:
    cell.font = Font(bold=True)
wb.save("report.xlsx")
```

## Примеры — pandas (чтение и аналитика)

### Прочитать и посмотреть

```python
import pandas as pd
df = pd.read_excel("data.xlsx")
print(df.shape)
print(df.head(10))
```

Конкретный лист — `pd.read_excel(path, sheet_name="Продажи")`.
Все листы сразу — `sheet_name=None` вернёт `dict` `{лист: DataFrame}`.

### Агрегации

```python
import pandas as pd
df = pd.read_excel("sales.xlsx")

# Сумма по клиентам
print(df.groupby("Клиент")["Сумма"].sum().sort_values(ascending=False).head(10))

# Среднее и количество в одном вызове
print(df.groupby("Менеджер")["Сумма"].agg(["sum", "mean", "count"]))
```

### Фильтр

```python
import pandas as pd
df = pd.read_excel("deals.xlsx")
paid = df[df["Статус"] == "Оплачен"]
big = df[df["Сумма"] > 1_000_000]
```

### CSV

```python
import pandas as pd
df = pd.read_csv("export.csv")
df.to_excel("export.xlsx", index=False)
```

### Объединение листов / файлов

```python
import pandas as pd
clients = pd.read_excel("clients.xlsx")
deals = pd.read_excel("deals.xlsx")
merged = clients.merge(deals, on="client_id", how="left")
merged.to_excel("merged.xlsx", index=False)
```

## Комбинированный сценарий: посчитать pandas'ом, оформить openpyxl'ом

```python
import pandas as pd
import openpyxl
from openpyxl.styles import Font

# 1. Считаем
df = pd.read_excel("sales.xlsx")
report = df.groupby("Клиент")["Сумма"].sum().sort_values(ascending=False).reset_index()

# 2. Сохраняем
report.to_excel("top_clients.xlsx", index=False)

# 3. Оформляем шапку
wb = openpyxl.load_workbook("top_clients.xlsx")
ws = wb.active
for cell in ws[1]:
    cell.font = Font(bold=True)
wb.save("top_clients.xlsx")
```
