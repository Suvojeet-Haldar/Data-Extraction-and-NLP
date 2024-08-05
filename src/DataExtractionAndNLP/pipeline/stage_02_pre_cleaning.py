from src.DataExtractionAndNLP.config.configuration import ConfigurationManager
from src.DataExtractionAndNLP.components.pre_cleaning import PreCleaning
from src.DataExtractionAndNLP import logger

STAGE_NAME = "Pre Cleaning stage"


class PreCleaningPipeline:
    def __init__(self):
        pass

    def main(self, data):
        logger.info("Inside pre cleaning main pipeline")
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        pre_cleaning = PreCleaning(config=data_ingestion_config)
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