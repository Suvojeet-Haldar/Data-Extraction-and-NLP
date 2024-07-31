# import os
# import urllib.request as request
# import zipfile
# from src.DataExtractionAndNLP import logger
# from src.DataExtractionAndNLP.utils.common import get_size
# from pathlib import Path
from src.DataExtractionAndNLP.entity.config_entity import (DataCleaningConfig)
# import requests
# from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from nltk.corpus import cmudict






class DataCleaning:
    def __init__(self, config: DataCleaningConfig):
        self.config = config

    def clean(self, data, metrics):
        with open(f'../../../artifacts/data_ingestion/{data[0]}_{data[1]}.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Remove all punctuation marks
            text = re.sub(r'[^\w\s]', '', text)

            # Remove stopwords
            stop_words = set(stopwords.words('english'))
            words = word_tokenize(text)
            cleaned_words = [word for word in words if word.isalpha() and word.lower() not in stop_words]

            # Calculating Word Count
            word_count = len(cleaned_words)

            complex_word_count = metrics[1]

            # Calculating Percentage of Complex Words
            percentage_complex_words = complex_word_count / word_count

            avg_sentence_length = metrics[0]

            # Calculating Fog Index
            fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

            # Calculating Average Words Per Sentence
            avg_words_per_sentence = word_count / len(sent_tokenize(text))