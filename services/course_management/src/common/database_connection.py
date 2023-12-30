import os

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure


class DBConnection:
    _instance = None

    def __new__(cls, *args, **kwargs) -> AsyncIOMotorClient:
        if cls._instance == None:
            print("------------------- hehe")
            cls._instance = AsyncIOMotorClient(os.getenv("DB_URL"))[os.getenv("DB")]
        return cls._instance


def get_db() -> AsyncIOMotorClient:
    try:
        yield DBConnection()
    except ConnectionFailure as e:
        raise ConnectionError("Failed to connect to the database.", e)
