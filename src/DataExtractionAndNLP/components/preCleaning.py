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






class PreCleaning:
    def __init__(self, config: DataCleaningConfig):
        self.config = config

    def calculate(self, data):
        with open(f'../../../artifacts/data_ingestion/{data[0]}_{data[1]}.txt', 'r', encoding='utf-8') as file:
            text = file.read()

            # Function to calculate average word length
            def average_word_length(text):
                words = word_tokenize(text)
                total_chars = sum(len(word) for word in words)
                num_words = len(words)
                return total_chars / num_words
            
            # Function to count syllables in a word
            def count_syllables(word):
                vowels = 'aeiouAEIOU'
                syllables = 0
                prev_char_vowel = False
                for char in word:
                    if char in vowels:
                        if not prev_char_vowel:
                            syllables += 1
                        prev_char_vowel = True
                    else:
                        prev_char_vowel = False
                return syllables
            
            # Function to count complex words (more than two syllables)
            def count_complex_words(text):
                words = word_tokenize(text)
                d = cmudict.dict()
                complex_words = [word for word in words if len(d.get(word.lower(), [])) > 2]
                return len(complex_words)
            
            # Function to calculate average sentence length
            def average_sentence_length(text):
                sentences = sent_tokenize(text)
                num_sentences = len(sentences)
                words = word_tokenize(text)
                num_words = len(words)
                return num_words / num_sentences

            # Calculate metrics
            avg_sentence_length = average_sentence_length(text)
            complex_word_count = count_complex_words(text)
            syllable_count = sum(count_syllables(word) for word in word_tokenize(text))
            personal_pronouns_count = len(re.findall(r'\b(I|we|my|ours)\b', text, flags=re.IGNORECASE))
            personal_pronouns_count+=len(re.findall(r'\b(us|Us|uS)\b', text))
            avg_word_length = average_word_length(text)

            metrics=[avg_sentence_length, complex_word_count, syllable_count, personal_pronouns_count, avg_word_length]

            return metrics