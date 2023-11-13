from pydantic import BaseModel
from typing import List
from bson import ObjectId
from beanie import Document


class Events(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
