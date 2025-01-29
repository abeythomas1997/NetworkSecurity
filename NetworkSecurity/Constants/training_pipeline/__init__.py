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

'''
Data Ingestion related constant start with  DATA_INGESTION_ var name

'''

DATA_INGESTION_COLLECTION_NAME: str=""
DATA_INGESTION_DATABASE_NAME :str=""
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="Ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:str="0.2"
