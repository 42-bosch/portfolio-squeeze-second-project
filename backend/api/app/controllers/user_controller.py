from fastapi import HTTPException, status

from app.database import collection, database
from app.schemas.user_schema import serialize_users, UserCreateSchema


def get_users() -> list:
    users = serialize_users(collection.users.find())
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Users not found"
        )
    return users


def get_user_by_name(name: str) -> list:
    user = serialize_users(collection.users.find({"name": name}))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


def create_user(user: UserCreateSchema) -> dict:
    user = collection.users.insert_one(user.dict())
    return {"message": "User created successfully"}
