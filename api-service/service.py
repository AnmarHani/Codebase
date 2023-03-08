from fastapi import FastAPI
import api_routes

app = FastAPI()


app.include_router(api_routes.router)