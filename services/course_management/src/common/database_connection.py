import os
from motor.motor_asyncio import AsyncIOMotorClient

class DBConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("------------------- hehe")
            cls._instance = AsyncIOMotorClient(os.getenv("DB_URL"))[os.getenv("DB")]
        return cls._instance