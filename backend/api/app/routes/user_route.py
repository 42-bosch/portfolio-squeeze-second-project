from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

import app.controllers.user_controller as user_controller
from app.schemas.user_schema import UserCreateSchema, UserBaseSchema


user_router = APIRouter(prefix="/user")


@user_router.get("/")
def get_users() -> JSONResponse:
    users = user_controller.get_users()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "success", "users": users},
    )


@user_router.post("/")
def create_user(user: UserCreateSchema) -> JSONResponse:
    new_user = UserBaseSchema(
        name=user.name,
        email=user.email,
        hashedPassword=user.password,
    )


    response = user_controller.create_user(new_user)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": "success", "message": response},
    )

@user_router.get("/{name}")
def get_user_by_name(name: str) -> JSONResponse:
    user = user_controller.get_user_by_name(name)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "success", "user": user},
    )
