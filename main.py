import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

from bot.handler import get_all_routers
from config import config
from db.engine import init_db
from middleware.logging.logger import setup_logger

setup_logger(log_level=config.LOG_LEVEL)


async def on_startup(bot: Bot) -> None:
    await init_db()
    logger.info("Database initialized")


async def main() -> None:
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    for router in get_all_routers():
        dp.include_router(router)

    dp.startup.register(on_startup)

    logger.info("Starting bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
