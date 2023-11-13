# from dotenv import load_dotenv
# from pymongo import MongoClient
# import os

# load_dotenv()
# async def connect():
#     try:
#         client = MongoClient(os.environ.get("mongo_url"))
#         db = client.test_db
#         db.Users.find_one
#         print("dabase connected")
#         return db
#     except Exception as err:
#         print(err)

# switch to beanie(async orm)
from models.users import User
from models.events import Events
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()
import os

mongo_uri = os.getenv("MONGO_URI")


async def connect():
    try:
        client = AsyncIOMotorClient(mongo_uri)
        await init_beanie(database=client["events"], document_models=[User, Events])
        print("database connected")
    except Exception as err:
        print(err)


async def addUser():
    user = User(username="tim", email="tim@gmail.com", password="1234")
    await user.create()
