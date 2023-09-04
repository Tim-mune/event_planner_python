from fastapi import APIRouter, status, HTTPException
from models.users import User, UserSignIn

user_router = APIRouter(tags=["users"])
users = {}


@user_router.post("/signup")
async def register_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            detail="user already exists", status_code=status.HTTP_400_BAD_REQUEST
        )
    users[data.email] = data
    return {"msg": "register successful"}


@user_router.post("/signin")
async def login_user(data: UserSignIn):
    if data.email not in users:
        raise HTTPException(
            detail="email is not registred", status_code=status.HTTP_404_NOT_FOUND
        )
    elif users[data.email].password != data.password:
        raise HTTPException(
            detail="invalid credentials", status_code=status.HTTP_400_BAD_REQUEST
        )
    return {"msg": "user signin success"}
