import asyncio
from fastapi import APIRouter
from services.journal import journal_service
from schemas.schedule import LoginRequest

router = APIRouter(prefix="/Schedule", tags=["College"])

service = journal_service()

@router.post("/get-schedule-data")
async def get_schedule_data(data: LoginRequest):
    responce = await service.get_schedule_data(
        username=data.username,
        password=data.password
    )
    return responce
