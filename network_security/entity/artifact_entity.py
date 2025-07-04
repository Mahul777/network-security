# The main role of artifact_entity.py is to:
  # 📦 Define the output format of each pipeline step
  # 🔗 Make the pipeline modular and reusable
  # 📚 Help track and log pipeline outputs in an organized way

from dataclasses import dataclass

# ✅ Artifact for Data Ingestion
@dataclass
class DataIngestionArtifact:
    feature_store_path: str        # Path to full raw data (CSV)
    train_file_path: str           # Path to training data CSV
    test_file_path: str            # Path to testing data CSV


# ✅ Artifact for Data Validation
@dataclass
class DataValidationArtifact:
    validation_status: bool        # True if validation passed
    valid_data_path: str           # Path to valid (cleaned) dataset
    invalid_data_path: str         # Path to invalid rows if any
    validation_report_path: str    # Path to validation report (JSON/YAML)


# ✅ Artifact for Data Transformation
@dataclass
class DataTransformationArtifact:
    transformed_train_path: str    # Path to transformed train data
    transformed_test_path: str     # Path to transformed test data
    transformer_object_path: str   # Path to scaler/transformer.pkl
    target_encoder_path: str       # Path to label encoder/class encoder.pkl


# ✅ Artifact for Model Training
@dataclass
class ModelTrainerArtifact:
    model_path: str                # Path to saved trained model (.pkl)
    training_accuracy: float       # Accuracy on training set
    test_accuracy: float           # Accuracy on test set
    model_report_path: str         # Path to model evaluation report (optional)


# ✅ Artifact for Model Evaluation
@dataclass
class ModelEvaluationArtifact:
    is_model_accepted: bool        # Whether model is better than previous
    best_model_path: str           # Path to previous best model
    current_model_path: str        # Path to current model
    evaluation_report: str         # JSON/YAML summary of comparison


# ✅ Artifact for Model Deployment
@dataclass
class ModelPusherArtifact:
    saved_model_path: str          # Final exported model path
    model_registry_path: str       # Location in model registry (e.g., "s3://...")

