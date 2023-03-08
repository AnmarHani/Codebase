from fastapi import FastAPI
from user import user_routes
from utils.database import engine
app = FastAPI()

@app.on_event("startup")
async def startup():
    await engine.connect()

app.include_router(user_routes.router)

@app.on_event("shutdown")
async def shutdown():
    await engine.disconnect()