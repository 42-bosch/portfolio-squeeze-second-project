from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

client = MongoClient(config["DB_URL"])
database = client["project2"]


def verify_connection():
    try:
        client.admin.command("ping")
        return True
    except:
        return False
