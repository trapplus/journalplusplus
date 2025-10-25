from aiogram import Router
from aiogram.types import Message
# from aiogram.filters import Command

homework_router = Router()

@homework_router.message(commands=["/homework", "/дз"])
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, 'key': 'value'")
