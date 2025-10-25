from aiogram import Router

from src.bot.handlers.homework import homework_router
from src.bot.handlers.schedule import schedule_router
from src.bot.handlers.start import start_router

commutator = Router()

commutator.include_router(homework_router)
commutator.include_router(schedule_router)
commutator.include_router(start_router)
