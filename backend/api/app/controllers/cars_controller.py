from fastapi import HTTPException, status

from app.database import collection, database
from app.schemas.cars_schema import CarCreateSchema, serialize_car, serialize_cars

def get_cars() -> list:
    return serialize_cars(collection.find())

def create_car(car: CarCreateSchema) -> dict:
    maker = car.maker
    car_data = car.car.dict()
    
    existing_maker = collection.find_one({"maker.name": maker.name})
    if existing_maker:
        existing_maker["maker"]["cars"].append(car_data)
        collection.update_one({"_id": existing_maker["_id"]}, {"$set": existing_maker})
    else:
        new_maker = {"maker": {"name": maker.name, "cars": [car_data]}}
        collection.insert_one(new_maker)
    return {"message": "Car created successfully"}


def get_cars_by_maker(maker_name: str) -> list:
    maker_data = collection.find_one({"maker.name": maker_name})
    if not maker_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Maker not found"
        )
    return serialize_cars(maker_data.get("maker").get("cars", []))


def delete_car(car_id: str) -> dict:
    car = collection.find_one({"_id": car_id})
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Car not found"
        )
    collection.delete_one({"_id": car_id})
    return {"message": "Car deleted successfully"}