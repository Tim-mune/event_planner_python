from fastapi import APIRouter, status, HTTPException, Depends, Body
from models.users import User, UserSignIn
from db.connect import connect

user_router = APIRouter(tags=["users"])


@user_router.post("/signup")
async def register_user(data: User = Body(...), db=Depends(connect)) -> dict:
    print(dict(data)["email"])
    user_collection = db["Users"]
    existing_user = user_collection.find_one({"email": dict(User)["email"]})
    if existing_user:
        raise HTTPException(
            detail="invalid credentials", status_code=status.HTTP_201_CREATED
        )
    user_collection.insert_one(dict(data))
    return {"msg": "register successful"}


@user_router.post("/signin")
async def login_user(data: UserSignIn):
    return {"msg": "user signin success"}


@user_router.get("/users")
async def register_user(db=Depends(connect)) -> dict:
    user_collection = db["Users"]
    print(list(user_collection.find({})))
    return {"users": len(list(user_collection.find({})))}
