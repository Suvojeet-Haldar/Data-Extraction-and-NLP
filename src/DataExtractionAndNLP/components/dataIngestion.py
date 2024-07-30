import os
# import urllib.request as request
# import zipfile
from src.DataExtractionAndNLP import logger
# from src.DataExtractionAndNLP.utils.common import get_size
# from pathlib import Path
from src.DataExtractionAndNLP.entity.config_entity import (DataIngestionConfig)
import requests
from bs4 import BeautifulSoup



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def extraction(self, data):
        try:
            # Fetch the webpage content
            url=data[0]
            Class=data[1]
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the article title and text 
            # title = soup.select_one('h1.entry-title').get_text()
            article_text = soup.select_one(f'{Class}').get_text()

            # Save the extracted article to a text file
            output_file = os.path.join(self.config.root_dir, f'{url}_{Class}.txt')
            with open(output_file, 'w', encoding='utf-8') as f:
                # f.write(f"{title}\n")
                f.write(article_text)

            logger.info(f"Extracted article from {url} and saved to {output_file}")
        except Exception as e:
            logger.info(f"Error processing {url}: {e}")

        # if not os.path.exists(self.config.local_data_file):
        #     filename, headers = request.urlretrieve(
        #         url = self.config.source_URL,
        #         filename= self.config.local_data_file
        #     )
        #     logger.info(f"{filename} download! with following info: \n{headers}")
        # else:
        #     logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")



    def create_dir(self):
        path = self.config.root_dir
        os.makedirs(path, exist_ok=True)