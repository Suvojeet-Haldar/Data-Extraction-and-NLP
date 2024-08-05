from src.DataExtractionAndNLP.utils.common import get_name
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from src.DataExtractionAndNLP.entity.config_entity import (PostCleaningConfig)
import os



class PostCleaning:
    def __init__(self, config: PostCleaningConfig):
        self.config = config

    def create_sets(self):
        # Read positive and negative words from your .txt files
        def read_words_from_file(file_path):
            with open(file_path, 'r', encoding='latin-1') as file:
                return [word.strip() for word in file.readlines()]

        # Read words from the files
        positive_words = read_words_from_file(self.config.positive_file_path)
        negative_words = read_words_from_file(self.config.negative_file_path)

        # Create sets for positive and negative words
        positive_set = set(positive_words)
        negative_set = set(negative_words)

        return positive_set, negative_set



    def calculate(self, metrics, data, positive_set, negative_set):
        if isinstance(data, list):
            filename = get_name(data)
        else:
            filename = "pasted_text.txt"
            
        output_file = os.path.join(self.config.root_dir, filename)

        with open(output_file, 'r', encoding='utf-8') as file:
            cleaned_text = file.read()

            # Tokenize the cleaned text
            tokens = nltk.word_tokenize(cleaned_text)

            # Calculate positive and negative scores
            positive_score = sum(1 for word in tokens if word.lower() in positive_set)
            negative_score = sum(-1 for word in tokens if word.lower() in negative_set) * -1

            # Calculate polarity and subjectivity scores
            total_words = len(tokens)
            polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
            subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)

            # Calculating Word Count
            cleaned_words_list = [word for word in tokens]
            word_count = len(cleaned_words_list)

            # Calculating Percentage of Complex Words
            complex_word_count = metrics['complex_word_count']
            percentage_complex_words = complex_word_count / word_count

            # Calculating Fog Index
            avg_sentence_length = metrics['avg_sentence_length']
            fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

            # Calculating Average Words Per Sentence
            avg_words_per_sentence = word_count / len(sent_tokenize(cleaned_text))

            metrics.update({"positive_score": positive_score, "negative_score": negative_score, "polarity_score": polarity_score, "subjectivity_score": subjectivity_score, "word_count": word_count, "percentage_complex_words": percentage_complex_words, "fog_index": fog_index, "avg_words_per_sentence": avg_words_per_sentence})

            # Removing the file just before returning the metrics for the final time to save space, this is optional
            file.close()
            os.remove(output_file)

            return metrics