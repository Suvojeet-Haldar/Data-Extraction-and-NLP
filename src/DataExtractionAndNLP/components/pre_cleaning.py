import os
from src.DataExtractionAndNLP import logger
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import cmudict
import re
from src.DataExtractionAndNLP.entity.config_entity import (DataIngestionConfig)
from src.DataExtractionAndNLP.utils.common import get_name






class PreCleaning:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def calculate(self, data):
        logger.info("Inside calculate function (pre-cleaning component)")
        if isinstance(data, list):
            filename = get_name(data)
            
            output_file = os.path.join(self.config.root_dir, filename)

            with open(output_file, 'r', encoding='utf-8') as file:
                text = file.read()
        else:
            text = data
            
        logger.info("Inside pre cleaning main pipeline")
        
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

        metrics={"avg_sentence_length":avg_sentence_length, "complex_word_count":complex_word_count, "syllable_count":syllable_count, "personal_pronouns_count":personal_pronouns_count, "avg_word_length":avg_word_length}
        
        logger.info(f"Pre-Cleaning Metrics Calculated Successfully")
        return metrics
