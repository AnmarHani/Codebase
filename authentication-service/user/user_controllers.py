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
from utils.database import db
import json
import pymongo

async def create_user():
    # create user
    user = user_model.User(name="Naif")
    db.users.insert_one(user.__dict__)
    return {"msg":f"saved with name :)!"}

async def get_user():
    users = db.users.find({})
    print(pymongo.dumps(list(users)))
    return {"users":list(users)}