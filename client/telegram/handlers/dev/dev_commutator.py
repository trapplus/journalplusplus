from aiogram import Router

from . import log, status, stop

commutator = Router()

commutator.include_router(log.router)
commutator.include_router(status.router)
commutator.include_router(stop.router)
