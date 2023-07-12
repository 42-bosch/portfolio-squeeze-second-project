from datetime import datetime
from pydantic import BaseModel, validator
from typing import List, Optional
from bson.objectid import ObjectId


def serialize_user(user) -> dict:
    return {
        "id": str(user.get("_id")),
        "name": user.get("name"),
        "createdAt": str(user.get("createdAt")),
        "updatedAt": str(user.get("updatedAt")),
    }


def serialize_users(users) -> list:

    return [serialize_user(user) for user in users]


class UserBaseSchema(BaseModel):
    id: str | None = None
    name: Optional[str] = None
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


class UserCreateSchema(UserBaseSchema):
    pass


class UserResponseSchema(BaseModel):
    status: str
    user: UserBaseSchema


class UsersResponseSchema(BaseModel):
    status: str
    users: List[UserBaseSchema]
