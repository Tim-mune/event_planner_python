from dotenv import load_dotenv, find_dotenv
from beanie import init_beanie, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from documents.User import Users
import os

load_dotenv()


async def connect():
    try:
        client = AsyncIOMotorClient(os.environ.get("mongo_url"))
        await init_beanie(database=client.db_name, document_models=[Users])
        print("data base connected")
        pass
    except Exception as err:
        print(err)
