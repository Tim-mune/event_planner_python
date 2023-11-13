from pydantic import EmailStr
from models.events import Events
from typing import List, Optional
from pydantic import BaseModel
from beanie import Document


class User(Document):
    username: str
    email: EmailStr
    password: str
    events: Optional[List[Events]]


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
