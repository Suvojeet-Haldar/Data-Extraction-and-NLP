from src.DataExtractionAndNLP.utils.common import get_name
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from src.DataExtractionAndNLP.entity.config_entity import (DataIngestionConfig)
import os



class Cleaning:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def clean(self, data):
        if isinstance(data, list):
            filename = get_name(data)
            
            output_file = os.path.join(self.config.root_dir, filename)

            with open(output_file, 'r', encoding='utf-8') as file:
                text = file.read()
        else:
            text = data
            output_file = os.path.join(self.config.root_dir, "pasted_text.txt")

        # Remove all punctuation marks
        text = re.sub(r'[^\w\s]', '', text)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text)
        cleaned_words_list = [word for word in words if word.isalpha() and word.lower() not in stop_words]

        # Join the filtered tokens back into a cleaned string
        cleaned_text = ' '.join(cleaned_words_list)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)
    