import asyncio
import logging
import sys
from os import getenv

from aiogram.filters import CommandStart
from aiogram.types import Message


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This test command handler `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
