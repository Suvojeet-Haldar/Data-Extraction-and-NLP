from src.DataExtractionAndNLP.constants import *
from src.DataExtractionAndNLP.utils.common import read_yaml, create_directories
from src.DataExtractionAndNLP.entity.config_entity import (DataIngestionConfig, PostCleaningConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])

  
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir ,
            unzip_data_dir=config.unzip_data_dir
        )

        return data_ingestion_config
    
    def get_post_cleaning_config(self) -> PostCleaningConfig:
        config = self.config.post_cleaning

        post_cleaning_config = PostCleaningConfig(
            root_dir=config.root_dir,
            positive_file_path=config.positive_file_path,
            negative_file_path=config.negative_file_path
        )

        return post_cleaning_config