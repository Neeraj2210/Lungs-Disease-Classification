from src.LD_Classifier.logger import logger
from src.LD_Classifier.Exception import CustomException
from src.LD_Classifier.pipeline.Stage_01_data_ingestion import  DataIngestionTrainingPipeline
from src.LD_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.LD_Classifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    error = CustomException(e, sys)
    logger.info(error.error_message)


STAGE_NAME = "Prepare base model"

try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    error = CustomException(e, sys)
    logger.info(error.error_message)


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    error = CustomException(e, sys)
    logger.info(error.error_message)




    
