from src.DataExtractionAndNLP import logger
from src.DataExtractionAndNLP.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.DataExtractionAndNLP.pipeline.stage_02_pre_cleaning import PreCleaningPipeline
# from DataExtractionAndNLP.pipeline.stage_03_training import ModelTrainingPipeline
# from DataExtractionAndNLP.pipeline.stage_04_evaluation import EvaluationPipeline

# logger.info("Welcome to my custom log")

data=['https://insights.blackcoffer.com/ml-and-ai-based-insurance-premium-model-to-predict-premium-to-be-charged-by-the-insurance-company/', 'div', 'td-post-content tagdiv-type']

data[2]=data[2].replace(" ", ".")

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main(data)
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Pre Cleaning stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   pre_cleaning = PreCleaningPipeline()
   metrics = pre_cleaning.main(data)
   logger.info(f"{metrics}\n\nx==========x")
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




# STAGE_NAME = "Training"
# try: 
#    logger.info(f"*******************")
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#    model_trainer = ModelTrainingPipeline()
#    model_trainer.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e






# STAGE_NAME = "Evaluation stage"
# try:
#    logger.info(f"*******************")
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#    model_evalution = EvaluationPipeline()
#    model_evalution.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

# except Exception as e:
#         logger.exception(e)
#         raise e