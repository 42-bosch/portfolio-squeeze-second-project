from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.schemas.cars_schema import CarCreateSchema
import app.controllers.cars_controller as cars_controller

cars_router = APIRouter(prefix="/cars")

@cars_router.get("/")
def get_cars() -> JSONResponse:
    cars = cars_controller.get_cars()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "success", "cars": cars},
    )

@cars_router.post("/")
def create_car(car: CarCreateSchema) -> JSONResponse:
    response = cars_controller.create_car(car)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": "success", "message": response},
    )


@cars_router.get("/maker/{maker_name}")
def get_cars_by_maker(maker_name: str) -> JSONResponse:
    cars = cars_controller.get_cars_by_maker(maker_name)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "success", "cars": cars},
    )


@cars_router.delete("/{car_id}")
def delete_car(car_id: str) -> JSONResponse:
    response = cars_controller.delete_car(car_id)
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={"status": "success", "message": response},
    )