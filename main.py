# The main.py file is the starting point or entry script for your machine learning pipeline project.

# | ✅  | Purpose                                                           |
# | -- | ----------------------------------------------------------------- |
# | 🔁 | Trigger the **entire pipeline**, step by step                     |
# | 🧪 | **Test** if the components (like Data Ingestion) are working      |
# | 🔧 | Initialize configuration classes and pipeline components          |
# | 📦 | **Return and log artifacts** like train/test paths or model files |
# | 🔍 | Easily debug by checking logs and prints from a single script     |

from network_security.components.data_ingestion import DataIngestion
from network_security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from network_security.logging.logger import logging
from network_security.exception.exception import NetworkSecurityException


if __name__ == "__main__":
    try:
        logging.info("🔁 Starting data ingestion...")

        # Step 1: Initialize training pipeline config
        training_pipeline_config = TrainingPipelineConfig()

        # Step 2: Pass it to data ingestion config
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)

        # Step 3: Initialize Data Ingestion component
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # Step 4: Trigger the data ingestion process
        artifact = data_ingestion.initiate_data_ingestion()

        # Step 5: Print the returned artifact
        print("✅ Data Ingestion Artifact:")
        print(artifact)

        logging.info("🏁 Data ingestion completed successfully.")

    except Exception as e:
        raise NetworkSecurityException(e)

