import os
from pymongo.mongo_client import MongoClient

MONGO_DB_URL = os.environ.get("MONGO_DB_URL")
if not MONGO_DB_URL:
    raise ValueError("MONGO_DB_URL environment variable not set")

client = MongoClient(MONGO_DB_URL)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)