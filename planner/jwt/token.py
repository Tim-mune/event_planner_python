from jose import jwt, JWTError
from fastapi import HTTPException, status
import os
from time import time
from datetime import datetime


secret_key = os.getenv("SECRET_KEY")


def get_token(user_id: str):
    # this is meant to get a token thats for a user by signing id
    payload = {"user": user_id, "expires": time() + 3600}

    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token


def verify_token(token: str):
    try:
        data = jwt.decode(token, secret_key, algorithms="HS256")
        expires = data.get("expires")
        if not expires:
            raise HTTPException(
                detail="no token supplied", status_code=status.HTTP_401_UNAUTHORIZED
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expires):
            raise HTTPException(
                detail="token expired", status_code=status.HTTP_403_FORBIDDEN
            )
        return data

    except JWTError:
        raise HTTPException(
            detail="invalid token", status_code=status.HTTP_400_BAD_REQUEST
        )
