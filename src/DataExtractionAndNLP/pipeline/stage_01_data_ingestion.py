# import joblib
# import numpy as np
# import pandas as pd
# from pathlib import Path
from src.DataExtractionAndNLP.config.configuration import ConfigurationManager
from src.DataExtractionAndNLP.components.data_ingestion import DataIngestion
from src.DataExtractionAndNLP import logger

STAGE_NAME = "Data Ingestion stage"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self, data):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        data_ingestion.extraction(data)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e