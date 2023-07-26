from fastapi import HTTPException, status
from jose import jwt
from datetime import datetime, timedelta
from bson.objectid import ObjectId

from app.config import SECRET_KEY, ALGORITHM
from app.database import collection_users
from app.schemas.user_schema import (
    serialize_users,
    serialize_user,
    UserCreateSchema,
    UserLoginSchema,
)


def get_users() -> str:
    users = serialize_users(collection_users.find())
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Users not found"
        )
    return users


def create_user(user: UserCreateSchema) -> dict:
    try:
        user_date = collection_users.insert_one(user.dict())

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Username already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"id": str(user_date.inserted_id)}


def get_user_by_username(username: str) -> list:
    user = serialize_users(collection_users.find({"username": username}))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


def login_user(user: UserLoginSchema, expires_delta: int = 30):
    db_user = collection_users.find_one({"username": user.username})
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if db_user["password"] != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = datetime.utcnow() + timedelta(minutes=expires_delta)
    payload = {"sub": user.username, "exp": access_token_expires}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "expires": access_token_expires.isoformat()}
