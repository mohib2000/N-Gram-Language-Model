import nltk  # This is a major NLP library

"""
This file generates the abc_corpus.txt file.
Do not use it if it is already included in the zip.

However, if you think you can parse the corpus better you can change the code below.
Parsing the corpus better means that when creating sentence less nonsense word are used.
"""

import nltk
from nltk.corpus import abc
from nltk.tokenize import word_tokenize, sent_tokenize
import re

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')

def clean_word(word):
    """
    Clean the word by removing non-alphabetic characters and converting to lowercase.
    """
    return re.sub(r'[^\w\s]', '', word).lower()

def handle_contractions(word, previous_word):
    """
    Expand contractions (e.g., "n't" to "not").
    """
    contractions = {"n't": "not", "'re": "are", "'s": "is", "'d": "would", "'ll": "will", "'ve": "have", "'m": "am"}
    if word in contractions:
        return [contractions[word]]
    if previous_word and word.lower() == "t" and previous_word.lower() in ["don", "doesn"]:
        return [previous_word[:-1], "not"]
    return [word]

def process_sentences(corpus):
    """
    Process sentences from the corpus: tokenization, cleaning, and handling contractions.
    """
    processed_sentences = []
    for sentence in corpus:
        # Join the list of words into a single string
        sentence_str = ' '.join(sentence)
        words = word_tokenize(sentence_str)
        processed_words = []
        for i, word in enumerate(words):
            cleaned_word = clean_word(word)
            if cleaned_word:
                expanded_words = handle_contractions(cleaned_word, processed_words[-1] if processed_words else None)
                processed_words.extend(expanded_words)
        processed_sentence = ' '.join(processed_words)
        processed_sentences.append(processed_sentence)
    return processed_sentences

# Processing sentences from the abc corpus
processed_sentences = process_sentences(abc.sents())

# Writing to file
with open("abc_corpus.txt", 'w', encoding='utf-8') as f:
    f.write("\n".join(processed_sentences))
