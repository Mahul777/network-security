# 🧠 In Simple Words:
# push_data.py helps you automate the process of uploading data from a CSV file into a MongoDB cloud database.

# | 🔢 Step | 🔧 Action                                           | 💬 Explanation                                        |
# | ------- | --------------------------------------------------- | ----------------------------------------------------- |
# | 1️⃣     | **Load MongoDB URL from `.env`**                    | To avoid hardcoding secrets like MongoDB credentials. |
# | 2️⃣     | **Read the CSV file using pandas**                  | CSV contains the phishing dataset you want to upload. |
# | 3️⃣     | **Clean the DataFrame (reset index)**               | Removes unnecessary index so MongoDB gets clean rows. |
# | 4️⃣     | **Convert DataFrame to list of JSON records**       | MongoDB stores data in BSON/JSON format.              |
# | 5️⃣     | **Connect to MongoDB using pymongo**                | Using credentials stored in `.env` file.              |
# | 6️⃣     | **Insert the JSON records into MongoDB collection** | The data is now stored in the cloud.                  |
# | 7️⃣     | **Print how many records were inserted**            | Confirms successful operation.                        |


import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from pymongo import MongoClient

from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

# Load environment variables
load_dotenv()
MONGODB_URL = os.getenv("MONGO_DB_URL")
print(MONGODB_URL) # mongodb+srv://coderninja1999:!mX8Qi.iiq-cRqZ@cluster0.97dlxe7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            pass  # Initialization if needed later
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_converter(self, file_path):
        """
        Read CSV file, clean index, and convert to JSON records
        """
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongodb(self, records, database, collection):
        """
        Connect to MongoDB and insert records
        """
        try:
            self.mongo_client = MongoClient(MONGODB_URL, tlsCAFile=ca)
            self.database = self.mongo_client[database]
            self.collection = self.database[collection]
            self.collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    # File path of the CSV
    file_path = "network_data\phisingData.csv"  # Update if your path differs 

    # Database and Collection names
    database = "Apoorvai"
    collection = "network_data"

    # Initialize the class
    network_obj = NetworkDataExtract()

    # Convert CSV to JSON records
    records = network_obj.csv_to_json_converter(file_path=file_path)
    print(records)

    # Insert records to MongoDB
    num_records = network_obj.insert_data_to_mongodb(records, database, collection)

    # Print results
    print(f"Inserted {num_records} records.")


