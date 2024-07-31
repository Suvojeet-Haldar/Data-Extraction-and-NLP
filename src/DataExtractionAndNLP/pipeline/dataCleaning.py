# import joblib
# import numpy as np
# import pandas as pd
# from pathlib import Path
from src.DataExtractionAndNLP.config.configuration import ConfigurationManager
from src.DataExtractionAndNLP.components.dataCleaning import DataCleaning
from src.DataExtractionAndNLP import logger

STAGE_NAME = "Data Cleaning stage"


class DataCleaningPipeline:
    def __init__(self):
        # self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        pass


    def clean(self, data, metrics):
        # prediction = self.model.predict(data)
        config = ConfigurationManager()
        data_cleaning_config = config.get_data_cleaning_config()
        data_cleaning = DataCleaning(config=data_cleaning_config)
        data_cleaning.clean(data, metrics)

        # return prediction

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataCleaningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e