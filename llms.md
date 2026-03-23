<!--
╔═════════════════════════════════════════════════════════════════════════════╗
║                        IMMUTABLE GOVERNANCE BLOCK                           ║
║           Этот блок не изменяется ни Claude, ни Codex, ни кем-либо          ║
║                      кроме владельца проекта                                ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║  ИЕРАРХИЯ РЕШЕНИЙ:                                                          ║
║    1. Владелец            - абсолютный приоритет, решения безоговорочны     ║
║    2. Claude              - архитектурные и технические решения             ║
║    3. Codex               - исполнение конкретных задач по готовому ТЗ      ║
║                                                                             ║
║  ПРАВИЛА ДЛЯ CODEX:                                                         ║
║    - Codex не проектирует архитектуру и не меняет структуру классов         ║
║    - Codex получает конкретную задачу ("реализуй X вот так") и выполняет    ║
║    - При конфликте решений Claude и Codex - приоритет у Claude              ║
║    - Codex не редактирует этот файл                                         ║
║                                                                             ║
║  ПРАВИЛА ДЛЯ CLAUDE:                                                        ║
║    - Claude не редактирует этот (IMMUTABLE GOVERNANCE) блок                 ║
║    - Claude не редактирует блок IMMUTABLE PROJECT SPEC ниже                 ║
║    - Изменения в остальных разделах помечаются: LLM Claude: <описание>::    ║
║    - Решения Claude считаются более технически корректными, чем Codex       ║
║                                                                             ║
║  ЦЕЛЬ ФАЙЛА:                                                                ║
║    Единый источник истины для AI-ассистентов. Проект движется               ║
║    в одном направлении, без архитектурных конфликтов.                       ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
-->

<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║                       IMMUTABLE PROJECT SPEC                                 ║
║     Базовые параметры проекта - не изменяются без решения владельца          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Проект:      Journal++                                                      ║
║  Тип:         Telegram-бот для взаимодействия с журналом Top Academy         ║
║  Назначение:  Демонстрационный, обучающий, личное использование              ║
║  Язык:        Python 3.13.x                                                  ║
║  Runtime:     CPython                                                        ║
║  Пакетный менеджер: uv                                                       ║
║  Инфраструктура: Docker                                                      ║
║  Фреймворк:   Aiogram 3.x                                                   ║
║  SDK:         top_journal_sdk (ручной реверс API Top Academy, без офиц. доки)║
║  HTTP:        httpx (async)                                                  ║
║  Валидация:   pydantic / pydantic-settings                                   ║
║  БД:          SQLite (dev) → PostgreSQL (prod)                               ║
║  Логирование: loguru                                                         ║
║  Прочее:      dotenv, starlette, asyncio                                     ║
║  Структура:   ООП                                                            ║
║  GH Repo:     https://github.com/trapplus/journalplusplus                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->

# Journal++ — AI Context Document

<!-- LLM Claude: добавлена секция логгера, обновлена структура проекта, задокументированы все реализованные решения:: -->

## Правила для AI-ассистентов

### Toolchain
- Python 3.13.x, CPython
- Пакеты устанавливаются и управляются через `uv` — не pip, не poetry
- Запуск: `uv run main.py`
- Docker используется для деплоя, локальная разработка без него

### Правила по коду
- Весь код асинхронный — `async/await` везде где есть I/O
- Никаких синхронных блокирующих вызовов в основном event loop
- ООП: логика разбита по классам, не процедурный стиль
- Type hints обязательны для публичных методов и классов
- Исключения обрабатываются явно, `bare except` запрещён

### Правила по логированию
- Единый логгер: `from middleware.logging.logger import logger`
- `setup_logger(log_level=config.LOG_LEVEL)` вызывается **первым** в `main.py`, до любых других импортов логгера
- Формат: `HH:mm:ss | LEVEL | module:function:line | message`
- Вывод: консоль (colorize=True) + файл `logs/journal.log` (rotation 10MB, retention 7 дней)
- Нигде в проекте не использовать `print()` и стандартный `logging`

### Правила по комментариям
- Язык: русский или английский — как удобнее в контексте
- Комментировать why и неочевидные решения, не what
- Никакого docstring-спама на каждый метод

### Важный контекст по SDK
`top_journal_sdk` — неофициальный, построен на ручном реверсе API Top Academy. Официальной документации нет. При обновлениях сервера SDK может сломаться. Баги в слое данных решаются в репо SDK: https://github.com/ITTopTools/top_journal_sdk

---

## Архитектура

```
main.py
   └── asyncio.gather()
          ├── Dispatcher (aiogram) — polling Telegram updates
          └── NotificationService.run() — polling Journal API
                    │
                    └── итерируется по users из DB батчами
                              └── JournalClient(token=user.token)
```

Всё крутится в **одном event loop**. Потоки не используются.

---

## Структура проекта

```
journalplusplus/
├── bot/
│   ├── __init__.py
│   └── handler/
│       ├── __init__.py        # get_all_routers() — реэкспорт всех роутеров
│       ├── attendance.py
│       ├── grades.py
│       ├── help.py
│       ├── homework.py
│       ├── login.py
│       └── schedule.py
├── db/
│   ├── __init__.py
│   └── engine.py              # init_db(), вызывается в on_startup
├── middleware/
│   ├── cors/
│   └── logging/
│       └── logger.py          # setup_logger(), единый логгер проекта
├── services/
│   ├── __init__.py
│   ├── homework/
│   ├── login/
│   └── notification/          # NotificationService (M8)
├── config.py                  # pydantic-settings, читает .env
├── main.py                    # точка входа
├── Dockerfile
├── pyproject.toml
├── uv.lock
├── .env.example
├── llms.md                    # этот файл
└── NOTIFICATIONS.md           # детальная документация поллера уведомлений
```

---

## Реализованные решения

### `config.py`
`pydantic-settings`, `BaseSettings`. Поля: `BOT_TOKEN`, `LOG_LEVEL`, `DB_TYPE`, `DB_URL`.
`model_validator` проверяет что `DB_TYPE` один из `{sqlite, postgres, mysql}`.
`BOT_TOKEN` без дефолта — обязательное поле, падает при старте если не задан.
Pyright ругается на отсутствие дефолта — ложное срабатывание, в рантайме корректно.

```python
model_config = {"env_file": ".env"}
```

### `bot/handler/__init__.py`
Реэкспортирует все роутеры через `get_all_routers() -> list[Router]`.

```python
# main.py
for router in get_all_routers():
    dp.include_router(router)
```

Роутеры в каждом хендлере инициализируются через:
```python
from aiogram import Router
router = Router(name=__name__)
```

### `middleware/logging/logger.py`
`setup_logger(log_level)` настраивает loguru.
Формат: `HH:mm:ss | LEVEL | name:function:line | message`.
Консоль (colorize) + файл с rotation 10MB / retention 7 дней.

### `main.py`
```python
setup_logger(log_level=config.LOG_LEVEL)   # первым делом

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

for router in get_all_routers():
    dp.include_router(router)

dp.startup.register(on_startup)            # init_db здесь

await dp.start_polling(bot)
```

`NotificationService` подключается через `asyncio.gather` на M8.

---

## Система уведомлений

**Проблема:** нет вебхуков, нет документированного API.

**Решение:** единый поллер по всем пользователям батчами.

```
BATCH_SIZE = 10      # параллельных запросов за раз
BATCH_DELAY = 2      # сек между батчами (защита от 429)
POLL_INTERVAL = 60   # сек между полными циклами
```

- `asyncio.gather(*tasks, return_exceptions=True)` — ошибка одного юзера не роняет цикл
- `bot.send_message()` работает в polling mode без ограничений
- Сравниваем данные с кэшем в DB, при изменении шлём уведомление

Подробнее: `NOTIFICATIONS.md`

---

## DB — схема таблицы users

```
users
├── chat_id            — Telegram chat id
├── token              — токен сессии журнала
├── notifications_on   — bool
├── cached_schedule    — JSON
├── cached_grades      — JSON
└── cached_hw_status   — JSON
```

---

## .env.example

```
BOT_TOKEN=your_telegram_bot_token
LOG_LEVEL=INFO
DB_TYPE=sqlite
DB_URL=sqlite:///./database.db
```

---

## Milestones

| # | Задача | Статус |
|---|---|---|
| M1 | Структура проекта, конфиг, Docker | ✅ |
| M2 | `config.py`, логгер, `main.py`, роутеры | ✅ |
| M3 | Авторизация, сохранение токена в DB | ⬜ |
| M4 | Расписание — просмотр | ⬜ |
| M5 | Оценки — просмотр | ⬜ |
| M6 | Посещаемость — просмотр | ⬜ |
| M7 | ДЗ — загрузка и скачивание файлов | ⬜ |
| M8 | NotificationService — поллинг и уведы | ⬜ |
| M9 | UI-полировка, клавиатуры, FSM | ⬜ |
| M10 | README, документация, демо | ⬜ |

---

## Известные ограничения

- API журнала не задокументирован — при обновлениях SDK может сломаться
- Задержка уведомлений до `POLL_INTERVAL` секунд
- SQLite только для разработки — при расширении мигрировать на PostgreSQL
- При 1000+ пользователях поллер стоит вынести в отдельный контейнер (arq / Celery + Redis)