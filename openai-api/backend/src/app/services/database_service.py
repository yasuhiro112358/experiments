from pymongo import MongoClient
from pymongo.database import Database
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../../../config/.env.dev'))

class DatabaseService:
    @staticmethod
    def get_mongo_client() -> MongoClient:
        return MongoClient(os.getenv("MONGO_URI"))

    @staticmethod
    def get_app_database() -> Database:
        client = DatabaseService.get_mongo_client()
        return client.appDatabase