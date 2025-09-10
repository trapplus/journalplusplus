from fastapi import APIRouter

from . import homework, integrity, schedule

commutator = APIRouter()

commutator.include_router(homework.router)
commutator.include_router(integrity.router)
commutator.include_router(schedule.router)
