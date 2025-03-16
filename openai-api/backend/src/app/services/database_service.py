import os
from pymongo import MongoClient
from pymongo.database import Database

class DatabaseService:
    @staticmethod
    def get_mongo_client() -> MongoClient:
        return MongoClient(os.getenv("MONGO_URI"))

    @staticmethod
    def get_app_database() -> Database:
        client = DatabaseService.get_mongo_client()
        return client.appDatabase