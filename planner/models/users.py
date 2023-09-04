from pydantic import BaseModel, EmailStr
from models.events import Events
from typing import List, Optional


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    events: Optional[List[Events]]


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
