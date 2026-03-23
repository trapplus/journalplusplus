# 🔔 Система уведомлений — Архитектура и решение

## Проблема

Сервер журнала Top Academy не предоставляет:
- Вебхуков
- Задокументированного публичного API
- Механизма подписки на события

SDK (`top_journal_sdk`) построен на **ручном реверсе API** и также не имеет документации по событиям.

При этом нужно отслеживать индивидуальные события для каждого пользователя:
- Изменения в расписании
- Новые оценки
- Отклонение / принятие ДЗ
- Отзывы на работы учеников
- Внутренние новости и ивенты

Поднимать отдельный сервис на каждого пользователя или группу — неприемлемо по ресурсам и сложности.

---

## Решение — Единый общий поллер

Один сервис итерируется по всем пользователям с включёнными уведомлениями, параллельно проверяет изменения и отправляет сообщения через бота.

```
┌─────────────────────────────────────┐
│         NotificationService         │
│                                     │
│  while True:                        │
│    users = db.get_all_users()       │
│                                     │
│    [user1] [user2] [user3] ...      │
│       ↓       ↓       ↓            │
│    gather(check, check, check)      │
│                                     │
│    sleep(60)                        │
└─────────────────────────────────────┘
```

---

## Реализация

### `services/notifications.py`

```python
from aiogram import Bot
from loguru import logger
import asyncio

BATCH_SIZE = 10  # кол-во пользователей в одном батче
POLL_INTERVAL = 60  # секунд между полными циклами
BATCH_DELAY = 2  # секунд между батчами (защита от 429)


class NotificationService:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def run(self):
        """Основной цикл — запускается параллельно с ботом."""
        while True:
            try:
                await self._poll_all_users()
            except Exception as e:
                logger.error(f"Poll cycle failed: {e}")
            await asyncio.sleep(POLL_INTERVAL)

    async def _poll_all_users(self):
        users = await db.get_users_with_notifications()

        for i in range(0, len(users), BATCH_SIZE):
            batch = users[i:i + BATCH_SIZE]
            tasks = [self._check_user(u) for u in batch]
            await asyncio.gather(*tasks, return_exceptions=True)
            await asyncio.sleep(BATCH_DELAY)

    async def _check_user(self, user):
        try:
            async with JournalClient(token=user.token) as client:
                await self._check_schedule(client, user)
                await self._check_grades(client, user)
                await self._check_homework(client, user)
        except Exception as e:
            logger.warning(f"User {user.id} check failed: {e}")

    async def _check_schedule(self, client, user):
        schedule = await client.get_schedule()
        if schedule != user.cached_schedule:
            await self.bot.send_message(user.chat_id, "📅 Расписание изменилось!")
            await db.update_schedule_cache(user.id, schedule)

    async def _check_grades(self, client, user):
        grades = await client.get_grades()
        if grades != user.cached_grades:
            await self.bot.send_message(user.chat_id, "📊 Появились новые оценки!")
            await db.update_grades_cache(user.id, grades)

    async def _check_homework(self, client, user):
        hw_status = await client.get_homework_status()
        if hw_status != user.cached_hw_status:
            await self.bot.send_message(user.chat_id, "📎 Статус ДЗ обновился!")
            await db.update_hw_cache(user.id, hw_status)
```

---

### Интеграция в `main.py`

```python
import asyncio
from aiogram import Bot, Dispatcher
from services.notifications import NotificationService
from db.engine import init_db
from config import config


async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    notification_service = NotificationService(bot)

    async def on_startup(bot: Bot):
        await init_db()

    dp.startup.register(on_startup)

    # Бот и поллер крутятся в одном event loop
    await asyncio.gather(
        dp.start_polling(bot),
        notification_service.run(),
    )


if __name__ == "__main__":
    asyncio.run(main())
```

---

## Почему не потоки

Весь стек (aiogram, httpx, sqlalchemy async) работает на `asyncio`. Смешивать с `threading` — race conditions и сложный дебаг.

`asyncio.gather()` запускает всё конкурентно в одном event loop — это правильный инструмент здесь.

---

## Защита от перегрузки сервера

| Параметр | Значение | Зачем |
|---|---|---|
| `BATCH_SIZE` | 10 | Не более 10 одновременных запросов |
| `BATCH_DELAY` | 2 сек | Пауза между батчами, защита от 429 |
| `POLL_INTERVAL` | 60 сек | Полный цикл раз в минуту |
| `return_exceptions=True` | — | Ошибка одного юзера не роняет цикл |

---

## Что хранить в БД на пользователя

```
users
├── chat_id           — куда слать сообщения
├── token             — токен сессии журнала
├── notifications_on  — bool, включены ли уведы
├── cached_schedule   — последнее известное расписание
├── cached_grades     — последние известные оценки
└── cached_hw_status  — последний статус ДЗ
```

---

## Известные ограничения

- API журнала не задокументирован — при обновлении сервера SDK может сломаться
- Нет гарантии моментальной доставки — задержка до `POLL_INTERVAL` секунд
- При большом числе пользователей (1000+) стоит вынести поллер в отдельный Docker-контейнер и использовать очередь задач (например, Celery + Redis или arq)

---

*Документ описывает текущее решение для демонстрационного и учебного использования.*