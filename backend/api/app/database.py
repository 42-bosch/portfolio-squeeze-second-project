from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

client = MongoClient(config["DB_URL"])
database = client.test
collection = database.users


def verify_connection():
    try:
        client.admin.command("ping")
        return True
    except:
        return False

