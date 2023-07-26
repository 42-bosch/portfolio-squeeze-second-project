from pymongo import MongoClient
from .config import MONGO_DETAILS

client = MongoClient(MONGO_DETAILS)
database = client["project2_fastapi"]


collection_users = database["users"]
collection_cars = database["cars"]


collection_users.create_index("username", unique=True)


def verify_connection():
    try:
        client.admin.command("ping")
        return True
    except:
        return False
