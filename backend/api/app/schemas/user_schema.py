from datetime import datetime
from pydantic import BaseModel, validator, EmailStr
from typing import List, Optional, Union
from bson.objectid import ObjectId


def serialize_user(user: Union[dict, None]) -> dict:
    if not user:
        return None

    serialized_user = {
        "name": user.get("name"),
        "email": user.get("email"),
        "createdAt": str(user.get("createdAt")),
        "updatedAt": str(user.get("updatedAt")),
    }
    return serialized_user


def serialize_users(users: List[dict]) -> List[dict]:
    if not users:
        return None

    serialized_users = [serialize_user(user) for user in users]
    return serialized_users


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr
    hashedPassword: str
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()

    @validator("createdAt", "updatedAt", pre=True, always=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UserCreateSchema(BaseModel):
    email: EmailStr
    name: str
    password: str
    confirmPassword: str


class UserResponseSchema(BaseModel):
    status: str
    user: UserBaseSchema


class UsersResponseSchema(BaseModel):
    status: str
    users: List[UserBaseSchema]
