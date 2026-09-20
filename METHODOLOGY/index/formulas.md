# Формулы метрик

Единый источник формул для пирамиды метрик.

## Уровень 1 — Бизнес

### MAU (Monthly Active Users)
```
MAU = Количество уникальных пользователей за последний месяц
```

### DAU (Daily Active Users)
```
DAU = Количество уникальных пользователей за день
```

### WAU (Weekly Active Users)
```
WAU = Количество уникальных пользователей за неделю
```

### Revenue
```
Revenue = Сумма выручки за период
```

### Market Share
```
Market Share = Доля компании на рынке (в %)
```

## Уровень 2 — Маржинальность

### LTV (Lifetime Value)
```
LTV = ARPU × Lifetime
```
Считается **по когортам**. Lifetime — средняя продолжительность жизни клиента в продукте.

### CAC (Customer Acquisition Cost)
```
CAC = Затраты на маркетинг / Число привлечённых платящих клиентов
```

### CPL (Cost Per Lead)
```
CPL = Затраты на маркетинг / Число лидов
```

### LTV / CAC
```
LTV / CAC ≥ 3  → здоровая экономика
```

### ARPU (Average Revenue Per User)
```
ARPU = Общий доход / Число активных пользователей
```

### ARPPU (Average Revenue Per Paying User)
```
ARPPU = Общий доход от платящих / Число платящих пользователей
```

### Contribution Margin
```
Contribution Margin = price per unit − variable cost per sale
```

## Уровень 3 — Лояльность

### Retention Rate
```
Retention = Число вернувшихся в продукт на N-период / Число пришедших впервые
```
Считается **по когортам**.

### Churn Rate
```
Churn Rate = Число ушедших за период / Число активных в начале периода
```

### C1 — конверсия в первую покупку
```
C1 = Число купивших впервые / Число увидевших продукт впервые
```

### C2 — конверсия во вторую покупку
```
C2 = Число купивших второй раз / Число купивших впервые
```

### NPS (Net Promoter Score)
```
NPS = (% промоутеров − % критиков) × 100%
```

### Sticky Factor
```
Sticky = DAU / MAU
```
Применим только при ежедневном паттерне использования.

### K-factor
```
K-factor = Среднее число приглашений от пользователя × Конверсия приглашения в регистрацию
```

## Уровень 4 — Ценность (NSM)

NSM формулируется индивидуально. Типовые шаблоны:

```
NSM = Successful actions per user per session
NSM = Time-to-first-value (median)
NSM = Money/Time saved per active user
NSM = Cumulative output (content created, tasks completed)
```

## Уровень 5 — Качество

### Orders / Match / Date per User или Session
```
{Event} per User = Общее число событий / Число активных пользователей
{Event} per Session = Общее число событий / Число сессий
```

### Баги — три разреза
```
Bugs per Session     = Crit.bugs / Sessions
Bugs per User        = Crit.bugs / Users
% Users with ≥1 bug  = Users with ≥1 crit.bug per month / Total active users × 100%
```

### Delivery Cost Share
```
Delivery Cost Share = Стоимость доставки / Общая стоимость заказа × 100%
```

### Delivery Time
```
Delivery Time = Среднее (или медиана) времени доставки заказа
```

## Доменные / специальные

### Проникновение по сотрудникам / транзакциям
```
Проникновение = Число использующих / Общее число × 100%
```

### Количество новых / активных бизнес-клиентов
```
New B2B clients = Число новых компаний за период
Active B2B clients = Число компаний с ≥1 действием за период
```
