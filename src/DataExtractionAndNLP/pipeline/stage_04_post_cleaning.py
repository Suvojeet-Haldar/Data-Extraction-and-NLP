from src.DataExtractionAndNLP.config.configuration import ConfigurationManager
from src.DataExtractionAndNLP.components.post_cleaning import PostCleaning
from src.DataExtractionAndNLP import logger

STAGE_NAME = "Post Cleaning stage"


class PostCleaningPipeline:
    def __init__(self):
        pass

    def main(self, metrics, data):
        config = ConfigurationManager()
        post_cleaning_config = config.get_post_cleaning_config()
        post_cleaning = PostCleaning(config=post_cleaning_config)
        positive_set, negative_set = post_cleaning.create_sets()
        metrics = post_cleaning.calculate(metrics, data, positive_set, negative_set)

        return metrics

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PostCleaningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e