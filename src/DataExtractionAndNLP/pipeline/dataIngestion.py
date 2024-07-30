# import joblib
# import numpy as np
# import pandas as pd
# from pathlib import Path
from src.DataExtractionAndNLP.config.configuration import ConfigurationManager
from src.DataExtractionAndNLP.components.dataIngestion import DataIngestion
from src.DataExtractionAndNLP import logger

STAGE_NAME = "Data Ingestion stage"


class DataIngestionPipeline:
    def __init__(self):
        # self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        pass


    def ingest(self, data):
        # prediction = self.model.predict(data)
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.create_dir()
        data_ingestion.extraction(data)

        # return prediction

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e