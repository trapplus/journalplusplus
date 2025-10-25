from aiogram import Router
from aiogram.types import Message
from src.utils.schedule import Schedule
from aiogram.filters import Command

schedule_router = Router()

@schedule_router.message(Command("schedule"))
async def command_schedule_handler(message: Message) -> None:
    data = Schedule()
    schedule_text = await data.get_schedule("test", "test")
    
    await message.answer(
        schedule_text,
        parse_mode="HTML"
    )
