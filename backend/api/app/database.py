from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

client = MongoClient(config["DB_URL"])
database = client.fastapi
collection = database.users
