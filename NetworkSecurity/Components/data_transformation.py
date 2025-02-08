import sys,os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from NetworkSecurity.Constants.training_pipeline import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS
from NetworkSecurity.Entity.artifacts_entity import (
    DataValidationArtifact,DataTransformationArtifact)

from NetworkSecurity.Entity.config_entity import DataTransformationConfig
from NetworkSecurity.Exception.exception import NetworkSecurityException 
from NetworkSecurity.Logging.logger import logging
from NetworkSecurity.Utils.main_utils.utils import save_numpy_array_data,save_object

class DataTransformation:
    def __init__(self,data_validation_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact:DataValidationArtifact=data_validation_artifact
            self.data_transformation_config:DataTransformationConfig=data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_csv)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def initiate_data_transformation(self) -> DataTransformationArtifact :
        