import asyncio
from fastapi import APIRouter
from services.schedule import journal_service
from schemas.schedule import LoginRequest

router = APIRouter(prefix="/Schedule", tags=["College"])

service = journal_service()

@router.post("/schedule")
async def get_schedule_data(data: LoginRequest):
    responce = await service.get_schedule_data_from(
        username=data.username,
        password=data.password
    )
    return responce
