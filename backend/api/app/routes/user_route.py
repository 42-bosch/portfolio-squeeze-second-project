from fastapi import APIRouter, HTTPException, status, File, UploadFile, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
import shutil

from app.depends import verify_token
from app.schemas.user_schema import (
    UserCreateSchema,
)


import app.controllers.user_controller as user_controller

user_router = APIRouter(prefix="/user")


@user_router.get("/", dependencies=[Depends(verify_token)])
def get_users() -> JSONResponse:
    users = user_controller.get_users()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "success", "users": users},
    )


@user_router.post("/")
def create_user(user: UserCreateSchema) -> JSONResponse:
    response = user_controller.create_user(user)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": "success", "message": response},
    )


@user_router.post("/login")
def login_user(user: OAuth2PasswordRequestForm = Depends()) -> JSONResponse:
    response = user_controller.login_user(user)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=response,
    )


@user_router.post("/uploadexcel", dependencies=[Depends(verify_token)])
def upload_excel(file: UploadFile = File(...)):
    with open(f"/cache/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}
