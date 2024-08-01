from src.DataExtractionAndNLP.config.configuration import ConfigurationManager
from src.DataExtractionAndNLP.components.cleaning import Cleaning
from src.DataExtractionAndNLP import logger

STAGE_NAME = "Cleaning stage"


class CleaningPipeline:
    def __init__(self):
        pass

    def main(self, data):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        clean = Cleaning(config=data_ingestion_config)
        clean.clean(data)

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = CleaningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e