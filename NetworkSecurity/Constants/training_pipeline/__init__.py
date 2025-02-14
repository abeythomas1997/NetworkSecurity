import os
import sys
import numpy as np
import pandas as pd


'''
defining common constant variable names

'''

TARGET_COLUMN="Result"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="Artifacts"
File_Name:str="phisingData.csv"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

MODEL_FILE_NAME = "model.pkl"

SAVED_MODEL_DIR =os.path.join("data_schema","schema.yaml")

SCHEMA_FILE_PATH =os.path.join("data_schema","schema.yaml")

'''
Data Ingestion related constant start with  DATA_INGESTION_ var name

'''

DATA_INGESTION_COLLECTION_NAME: str=""
DATA_INGESTION_DATABASE_NAME :str=""
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="Ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:str="0.2"


'''
Data Validation related constant start with  DATA_VALIDATION VAR NAME

'''
DATA_VALIDATION_DIR_NAME: str ="data_validation"
DATA_VALIDATION_VALID_DIR: str ="validated"
DATA_VALIDATION_INVALID_DIR :str ="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str ="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str ="report.yaml"
PREPROCESSING_OBJECT_FILE_NAME : str ="preprocessing.pkl"


'''
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME

'''

DATA_TRANSFORMATION_DIR_NAME: str="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str="transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str="transformed_object"



#KNN imputer to replace NAN values

DATA_TRANSFORMATION_IMPUTER_PARAMS:dict={
    "missing_values":np.nan,
    "n_neighbors":3,
    "weights":"uniform"
}

DATA_TRANSFORMATION_TRAIN_FILE_PATH:str="train.py"
DATA_TRANSFORMATION_TEST_FILE_PATH:str="test.py"


'''
Model trainer related constant starts with MODEL_TRAINER VAR NAME
'''

MODEL_TRAINER_DIR_NAME :str ="model_trainer"
MODEL_TRAINER_TRAINED_DIR: str="trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE:float=0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD: float =0.05

TRAINING_BUCKET_NAME = "networksecurity"
