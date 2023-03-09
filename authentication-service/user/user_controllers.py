# stripe vs moyasar
# digitalocean kubernetes vs smth
# nosql vs sql
# serverless
# one database vs microservices databases
# github teams
# discord
# clickup
# vscode
# dev(docker, kubernetes, python[fastapi], messages and queues and cache, MONGODB)
# figma
# midjourney
# emailing service

from . import user_model

async def create_user(request: user_model.UserTemplate):
    user = user_model.User(id=request.id, name=request.name, fullname=request.fullname, nickname=request.nickname)
    user.create()
    return {"msg":f"saved with name {request.name}!"}

async def get_user():
    return {"users":"no"}