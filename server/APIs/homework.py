import asyncio
from fastapi import APIRouter
from services.journal import journal_service
from schemas.schedule import LoginRequest

router = APIRouter(prefix="/Homework", tags=["College"])

service = journal_service()

@router.post("/get-homework-data")
async def get_homework_data():
    responce = None # TODO
    return responce
