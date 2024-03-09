from src.LD_Classifier.logger import logger
from src.LD_Classifier.Exception import CustomException
import os,sys


try:
    logger.info(f"First Log welcome 09-03-2024")
    a=1/0
    
except Exception as e:
        error = CustomException(e, sys)
        logger.info(error.error_message)