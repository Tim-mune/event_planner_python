from pydantic import BaseModel
from typing import List
from bson import ObjectId


class Events(BaseModel):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
