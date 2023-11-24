from pydantic import BaseModel
from typing import List
from bson.objectid import ObjectId
from beanie import Document
from datetime import datetime


class Location(BaseModel):
    longitude: float
    latitude: float
    address: float
    name: str
    altitude: float


class Events(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    event_date: str
    createdBy: str
    location: Location
    attending: List[str]

    class Settings:
        indexes = [{"fields": ["email"], "unique": True}]
