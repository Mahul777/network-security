# 📁 network_security/constants/training_pipeline/__init__.py
# 🎯 Purpose
# This file is like a settings file for your pipeline.
# Instead of writing 'train.csv' or 'network_data' everywhere, you store it once here,
# and reuse it everywhere in your project
import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""

TARGET_COLUMN = "Result"


"""
"""
# 🎯 Pipeline-level constants
PIPELINE_NAME = "network_security"
ARTIFACT_DIR = "artifacts"

# 📦 Data Ingestion constants
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"

# 📄 File names
FILE_NAME = "phisingData.csv"           # Raw data from MongoDB
TRAIN_FILE_NAME = "train.csv"            # Training set after split
TEST_FILE_NAME = "test.csv"              # Testing set after split

# 🔢 Split ratio for train-test
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

# 🛢️ MongoDB collection info
DATA_INGESTION_COLLECTION_NAME = "network_data"
DATA_INGESTION_DATABASE_NAME = "Apoorvai"
