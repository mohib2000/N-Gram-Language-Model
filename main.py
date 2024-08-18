from collections import defaultdict
from pathlib import Path
import autograder
import unittest
import numpy as np

# Function to parse a text file and return a list of sentences.
def parse_text_file(file):
    import re

    sentence_list = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            line = re.sub(r'[^A-Za-z\s]', '', line)  # Removing punctuation and digits
            words = line.split()  # Splitting the line into words
            sentence = ["<s>"] + words + ["</s>"]  # Adding start and end tokens
            sentence_list.append(sentence)

    return sentence_list

# Function to initialize the history for the n-gram model
def initialize_history(name):
    if name == 'unigram':
        return '<any>'
    elif name == 'bigram':
        return '<s>'
    elif name == 'trigram':
        return '<s>,<s>'

# Function to update the history based on the model type and the next word
def update_history(name, history, next_word):
    if name == 'bigram':
        return next_word
    elif name == 'trigram':
        return ','.join(history.split(',')[1:]) + ',' + next_word
    return history

# Function to create a defaultdict with a specified type
def create_defaultdict(type):
    return lambda: defaultdict(type)

# Function to create an n-gram model from a list of sentences
def make_ngram_model(sentences, name):
    count_dict = defaultdict(create_defaultdict(int))
    prob_dict = defaultdict(create_defaultdict(float))

    for sentence in sentences:
        # For unigram, we consider each word individually
        if name == 'unigram':
            for word in sentence[1:]:
                count_dict["<any>"][word] += 1

        # For bigram, we consider pairs of consecutive words
        elif name == 'bigram':
            for i in range(len(sentence) - 1):
                count_dict[sentence[i]][sentence[i + 1]] += 1

        # For trigram, we consider triplets of words
        elif name == 'trigram':
            sentence.insert(0,'<s>')
            for i in range(len(sentence) - 2):
                history = sentence[i] + ',' + sentence[i + 1]
                count_dict[history][sentence[i + 2]] += 1


    for history, word_counts in count_dict.items():
        total_count = sum(word_counts.values())
        for word, count in word_counts.items():
            prob_dict[history][word] = count / total_count

    return prob_dict

# Function to predict sentences using the n-gram model
def predict_sentence(model, name, n_sentences=10, max_sentence_len=10):
    rng = np.random.default_rng(seed=42)
    generated_sentences = []

    for _ in range(n_sentences):
        sentence = []
        history = initialize_history(name)

        for _ in range(max_sentence_len):
            word_dict = model[history]
            words, probabilities = zip(*word_dict.items())
            next_word = rng.choice(words, p=probabilities)

            if next_word == '</s>':
                break
            sentence.append(next_word)
            history = update_history(name, history, next_word)

        generated_sentences.append(' '.join(sentence) + '.')

    with open(f"generated_{name}_sentences.txt", "w") as file:
        for sentence in generated_sentences:
            file.write(sentence + "\n")

    return generated_sentences

# Other function definitions (parse_text_file, initialize_history, etc.) remain the same

def main():
    print("Welcome to the N-Gram Model Sentence Generator!")

    # Model selection with validation
    valid_models = {'1': 'unigram', '2': 'bigram', '3': 'trigram'}
    while True:
        print("\nChoose the n-gram model you want to use:")
        print("1. Unigram")
        print("2. Bigram")
        print("3. Trigram")
        model_choice = input("Enter your choice (1, 2, or 3): ").strip()
        if model_choice in valid_models:
            model_name = valid_models[model_choice]
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Number of sentences with validation
    while True:
        try:
            n_sentences = int(input("\nEnter the number of sentences to generate: ").strip())
            if n_sentences > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Maximum sentence length with validation
    while True:
        try:
            max_sentence_len = int(input("Enter the maximum length of each sentence: ").strip())
            if max_sentence_len > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Rest of the code for processing and generating sentences
    sentences = parse_text_file('abc_corpus.txt')  # Replace with the correct path to your file
    model = make_ngram_model(sentences, model_name)
    generated_sentences = predict_sentence(model, model_name, n_sentences, max_sentence_len)

    

if __name__ == "__main__":
    main()

