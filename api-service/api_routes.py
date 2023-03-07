from fastapi import APIRouter, Request
import api_controllers
router = APIRouter()

@router.get("/auth")
async def create_user(request: Request):
    return await api_controllers.test(request)