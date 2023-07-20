from datetime import datetime
from pydantic import BaseModel, validator
from typing import List, Optional

def serialize_maker(maker) -> dict:
    return {
        "name": maker.get("name"),
        "cars": [serialize_car(car) for car in maker.get("cars", [])],
    }

def serialize_car(car) -> dict:
    return {
        "year": car.get("year"),
        "model": car.get("model"),
        "market": car.get("market"),
        "createdAt": str(car.get("createdAt")),
        "updatedAt": str(car.get("updatedAt")),
    }

def serialize_cars(cars) -> list:
    return [serialize_car(car) for car in cars]

class CarSchema(BaseModel):
    year: Optional[int] = None
    model: Optional[str] = None
    market: Optional[str] = None
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()

    @validator("createdAt", "updatedAt", pre=True, always=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()

class MakerSchema(BaseModel):
    name: str
    cars: List[CarSchema] = []

class CarCreateSchema(BaseModel):
    maker: MakerSchema
    car: CarSchema

class CarResponseSchema(BaseModel):
    status: str
    car: CarCreateSchema

class CarsResponseSchema(BaseModel):
    status: str
    cars: List[CarCreateSchema]
