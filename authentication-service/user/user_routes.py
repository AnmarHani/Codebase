from fastapi import APIRouter
import os

router = APIRouter(
    prefix='/user'
)

@router.get("/")
async def create_user():
    return {"msg":os.environ['MONGODB_URL']}