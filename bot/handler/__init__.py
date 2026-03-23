# re-export all handler routers

from aiogram import Router

from bot.handler.attendance import router as attendance_router
from bot.handler.grades import router as grades_router
from bot.handler.help import router as help_router
from bot.handler.homework import router as homework_router
from bot.handler.login import router as login_router
from bot.handler.schedule import router as schedule_router

__all__ = [
    "attendance_router",
    "grades_router",
    "help_router",
    "homework_router",
    "login_router",
    "schedule_router",
]

def get_all_routers() -> list[Router]:
    """Return list with all router objects"""
    return [
        attendance_router,
        grades_router,
        help_router,
        homework_router,
        login_router,
        schedule_router,
    ]
