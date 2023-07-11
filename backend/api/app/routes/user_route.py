from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.database import collection
from app.schemas.user_schema import (
    serialize_user,
    serialize_users,
    UserBaseSchema,
    UserCreateSchema,
    UserResponseSchema,
    UsersResponseSchema,
)

user_router = APIRouter(prefix="/user")


@user_router.get("/", response_model=UsersResponseSchema)
def get_users() -> UsersResponseSchema:
    users = collection.find()
    if users is None:
        raise HTTPException(status_code=404, detail="No users found")

    return UsersResponseSchema(
        status="success",
        users=serialize_users(users),
    )


@user_router.post("/", response_model=UserResponseSchema)
def create_user(user: UserCreateSchema) -> UserResponseSchema:
    user = collection.insert_one(user.dict())
    if user is None:
        raise HTTPException(status_code=404, detail="User not created")

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content="User created successfully",
    )
