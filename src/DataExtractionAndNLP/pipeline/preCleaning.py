# import joblib
# import numpy as np
# import pandas as pd
# from pathlib import Path
from src.DataExtractionAndNLP.config.configuration import ConfigurationManager
from src.DataExtractionAndNLP.components.preCleaning import PreCleaning
from src.DataExtractionAndNLP import logger

STAGE_NAME = "Pre Cleaning stage"


class PreCleaningPipeline:
    def __init__(self):
        pass


    def calculate(self, data):
        # prediction = self.model.predict(data)
        config = ConfigurationManager()
        pre_cleaning_config = config.get_pre_cleaning_config()
        pre_cleaning = PreCleaning(config=pre_cleaning_config)
        metrics = pre_cleaning.calculate(data)

        return metrics

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PreCleaningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e