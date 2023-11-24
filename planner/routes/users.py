from fastapi import APIRouter, status, HTTPException, Depends, Body
from models.users import User, UserSignIn
from utils.sendEmail import sendEmail
from db.connect import connect

user_router = APIRouter(tags=["users"])


@user_router.post("/signup")
async def register_user(
    data: User = Body(...),
) -> dict:
    user_exists = await User.find_one(User.email == data.email)
    if user_exists:
        raise HTTPException(
            detail="user already exists", status_code=status.HTTP_400_BAD_REQUEST
        )
    user = User(**data.dict())
    await user.create()
    # send email
    sendEmail()
    return {"msg": "register successful"}


@user_router.post("/signin")
async def login_user(data: UserSignIn):
    user_exists = await User.find_one(User.email == data.email)
    return {"msg": "user signin success"}


@user_router.get("/users")
async def register_user(db=Depends(connect)) -> dict:
    user_collection = db["Users"]
    print(list(user_collection.find({})))
    return {"users": len(list(user_collection.find({})))}
