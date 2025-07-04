# 🎯 Purpose
# The data_ingestion.py file automates the process of getting your data from MongoDB, 
# saving it as raw CSV, splitting it into train/test, and returning all file paths 
# so the next steps (like feature engineering) can use them.


import os
import pandas as pd
import numpy as np
import pymongo
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.artifact_entity import DataIngestionArtifact
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

# Load environment variables (for MongoDB connection string) 
load_dotenv()

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        try:
            self.config = config
        except Exception as e:
            raise NetworkSecurityException(e)

    def export_collection_as_dataframe(self) -> pd.DataFrame:
        try:
            logging.info("📥 Connecting to MongoDB and exporting collection as DataFrame...")
            db_name = self.config.database_name
            col_name = self.config.collection_name

            client = pymongo.MongoClient(os.getenv("MONGO_DB_URL"))
            collection = client[db_name][col_name]
            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns:
                df.drop("_id", axis=1, inplace=True)

            df.replace({"na": np.nan, "all": np.nan}, inplace=True)

            logging.info("✅ Collection exported successfully.")
            return df
        except Exception as e:
            raise NetworkSecurityException(e)

    def export_data_to_feature_store(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            logging.info("💾 Saving full data to feature store...")
            feature_store_path = self.config.feature_store_file_path
            os.makedirs(os.path.dirname(feature_store_path), exist_ok=True)

            df.to_csv(feature_store_path, index=False, header=True)

            logging.info(f"✅ Feature store saved at: {feature_store_path}")
            return df
        except Exception as e:
            raise NetworkSecurityException(e)

    def split_and_save(self, df: pd.DataFrame):
        try:
            logging.info("🔀 Performing train/test split...")
            train_df, test_df = train_test_split(
                df,
                test_size=self.config.train_test_split_ratio,
                random_state=42
            )

            os.makedirs(os.path.dirname(self.config.train_file_path), exist_ok=True)

            train_df.to_csv(self.config.train_file_path, index=False, header=True)
            test_df.to_csv(self.config.test_file_path, index=False, header=True)

            logging.info("✅ Train and Test files saved.")
            return train_df, test_df
        except Exception as e:
            raise NetworkSecurityException(e)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("🚀 Starting data ingestion process...")

            df = self.export_collection_as_dataframe()
            df = self.export_data_to_feature_store(df)
            train_df, test_df = self.split_and_save(df)

            artifact = DataIngestionArtifact(
                feature_store_path=self.config.feature_store_file_path,
                train_file_path=self.config.train_file_path,
                test_file_path=self.config.test_file_path
            )

            logging.info("🏁 Data ingestion completed successfully.")
            return artifact
        except Exception as e:
            raise NetworkSecurityException(e)
