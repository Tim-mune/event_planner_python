from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os

load_dotenv()


async def connect():
    try:
        client = MongoClient(os.environ.get("mongo_url"))
        db = client.fastapi_test
        print("dabase connected")
        return db
    except Exception as err:
        print(err)
