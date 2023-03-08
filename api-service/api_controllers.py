from fastapi import Request
import requests

async def test(request: Request):
    response = requests.get("http://authentication-service:8081/user/create")
    return {"msg": response.text}

async def test_two(request: Request):
    response = requests.get("http://authentication-service:8081/user/get")
    print(response.__dict__)
    return {"msg": response.text}