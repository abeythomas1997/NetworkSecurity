from NetworkSecurity.Components.data_ingestion import DataIngestion
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logging.logger import logging
from NetworkSecurity.Entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,DataTrainerConfig
from NetworkSecurity.Entity.config_entity import TrainingPipelineConfig
from NetworkSecurity.Components.data_validation import DataValidation
from NetworkSecurity.Components.data_transformation import DataTransformation
from NetworkSecurity.Components.model_trainer import ModelTrainer

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("Initiate the data transformation")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("data Transformation Completed")
        logging.info("Model Training sstared")

        data_trainer_config=DataTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(data_trainer_config,data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")


        
    except Exception as e:
           raise NetworkSecurityException(e,sys)
