from src.DataExtractionAndNLP import logger
from src.DataExtractionAndNLP.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.DataExtractionAndNLP.pipeline.stage_02_pre_cleaning import PreCleaningPipeline
from src.DataExtractionAndNLP.pipeline.stage_03_cleaning import CleaningPipeline
from src.DataExtractionAndNLP.pipeline.stage_04_post_cleaning import PostCleaningPipeline

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




STAGE_NAME = "Cleaning stage"
try: 
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   cleaning = CleaningPipeline()
   cleaning.main(data)
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e





STAGE_NAME = "Post Cleaning stage"
try: 
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   post_cleaning = PostCleaningPipeline()
   metrics = post_cleaning.main(metrics, data)
   logger.info(f"{metrics}\n\nx==========x")
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e