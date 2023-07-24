from datetime import datetime
from pydantic import BaseModel, validator
from bson.objectid import ObjectId

from typing import List, Optional
from bson.objectid import ObjectId


def serialize_user(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user.get("username"),
        "createdAt": str(user.get("createdAt")),
        "updatedAt": str(user.get("updatedAt")),
    }


def serialize_users(users) -> list:
    return [serialize_user(user) for user in users]


class UserBaseSchema(BaseModel):
    username: str
    password: str
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()

    @validator("createdAt", "updatedAt", pre=True, always=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()

    @validator("password")
    def password_length(cls, value: str) -> str:
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters")
        return value



    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UserCreateSchema(UserBaseSchema):
    pass

class UserLoginSchema(BaseModel):
    username: str
    password: str


class UserResponseSchema(BaseModel):
    status: str
    user: UserBaseSchema


class UsersResponseSchema(BaseModel):
    status: str
    users: List[UserBaseSchema]
