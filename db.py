from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() 

class DB:
    def __init__(self):
        self.colection = self.connection_to_db()

    @staticmethod
    def connection_to_db():
        try:
            uri = os.getenv("mongodb://localhost:27017/")
            client = MongoClient(uri)

            db = client["terrorists"]
            colection = db["top_threats"]
            return colection
        except Exception:
            return None


    def insert_data(self,data):
        self.colection.insert_many(data)


