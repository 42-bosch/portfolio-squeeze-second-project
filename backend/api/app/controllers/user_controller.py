from fastapi import HTTPException, status

from app.database import collection
from app.schemas.user_schema import (
    serialize_user,
    serialize_users,
    UserCreateSchema,
)


def get_users() -> list:
    users = serialize_users(collection.find())
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Users not found"
        )
    return users


def create_user(user: UserCreateSchema) -> dict:
    user = collection.insert_one(user.dict())
    return {"message": "User created successfully"}


def get_user_by_name(name: str) -> list:
    user = serialize_users(collection.find({"name": name}))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user
