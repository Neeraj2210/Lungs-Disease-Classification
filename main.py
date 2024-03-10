from src.LD_Classifier.logger import logger
from src.LD_Classifier.Exception import CustomException
from src.LD_Classifier.pipeline.Stage_01_data_ingestion import  DataIngestionTrainingPipeline
import os,sys


STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        error = CustomException(e, sys)
        logger.info(error.error_message)

    
