from aiogram import Router
from aiogram.types import Message
# from aiogram.filters import Command

schedule_router = Router()

@schedule_router.message(commands=["/sсhedule", "/расписание"])
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, 'key': 'value'")
