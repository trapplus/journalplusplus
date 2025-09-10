from fastapi import APIRouter

router = APIRouter(prefix="/Homework", tags=["College"])

@router.get("/homework")
def get_homework_data():
    return {"hw":0}
