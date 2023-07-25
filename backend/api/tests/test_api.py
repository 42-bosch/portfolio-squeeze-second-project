import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database import collection

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    # You can optionally clear the database before running the tests
    # collection.delete_many({})
    pass

@pytest.fixture(autouse=True)
def mock_database_connection(monkeypatch):
    # Replace the actual database connection with a mock database connection
    # For example, if you are using a MongoDB client, you can use a mock in-memory database like mongomock
    import mongomock

    monkeypatch.setattr("app.database.collection", mongomock.MongoClient().db.collection)


def test_create_car(setup_db, mock_database_connection):
    # Given
    car_data = {
        "maker": {
            "name": "Acura",
            "cars": [
                {
                    "year": 2021,
                    "model": "ILX",
                    "market": "US, Canada"
                }
            ]
        },
        "car": {
            "year": 2021,
            "model": "ILX",
            "market": "US, Canada"
        }
    }

    # When
    response = client.post("/cars/", json=car_data)

    # Then
    assert response.status_code == 201
    assert response.json()["status"] == "success"
    assert response.json()["message"] == {"message": "Car created successfully"}

def test_get_cars(setup_db, mock_database_connection):
    # When
    response = client.get("/cars/")

    # Then
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["cars"]) > 0

def test_get_cars_by_maker(setup_db, mock_database_connection):
    # Given
    maker_name = "Acura"

    # When
    response = client.get(f"/cars/maker/{maker_name}")

    # Then
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["cars"]) > 0

def test_delete_car(setup_db, mock_database_connection):
    # Given
    car_data = {
        "maker": {
            "name": "Acura",
            "cars": [
                {
                    "year": 2021,
                    "model": "ILX",
                    "market": "US, Canada"
                }
            ]
        },
        "car": {
            "year": 2021,
            "model": "ILX",
            "market": "US, Canada"
        }
    }
    response = client.post("/cars/", json=car_data)
    car_id = response.json()["message"]["_id"]

    # When
    response = client.delete(f"/cars/{car_id}")

    # Then
    assert response.status_code == 202
    assert response.json()["status"] == "success"
    assert response.json()["message"] == {"message": "Car deleted successfully"}
