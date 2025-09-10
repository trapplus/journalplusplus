from aiogram import Router, types
from aiogram.filters import Command
from aiogram.filters.command import CommandObject

router = Router() 

@router.message(Command("log"))
async def cmd_log(message: types.Message, command: CommandObject):
    request = ""
    await message.answer("log")
