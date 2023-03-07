from fastapi import Request
import requests
import json

async def test(request: Request):
    response = requests.get("http://authentication-service:8081/user/")
    return {"msg": response.text}