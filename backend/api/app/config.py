from dotenv import dotenv_values



config = dotenv_values(".env")


MONGO_DETAILS = config["DB_URL"]
DATABASE = config["DB_NAME"]

SECRET_KEY = config["SECRET_KEY"]
ALGORITHM = config["ALGORITHM"]
TOKEN_EXPIRE_MINUTES = int(config["TOKEN_EXPIRE_MINUTES"])
