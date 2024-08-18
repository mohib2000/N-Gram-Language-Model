The problem statement for the project is defined here:  https://joshhug.github.io/LeidenITP/assignments/assignment3/

# N-Gram-Language-Model
This repository contains an implementation of a word n-gram language model, a foundational concept in natural language processing (NLP). The project is structured to demonstrate how to build and use n-gram models to predict sequences of words based on a given corpus.

Project Overview

In this project, the primary goal was to implement and understand the workings of n-gram models, which are probabilistic models used for predicting the next item in a sequence, such as a word in a sentence. N-grams can be of different orders, with the most common being:

    Unigram: Predicts the next word without considering the previous words.
    Bigram: Predicts the next word based on the previous word.
    Trigram: Predicts the next word based on the previous two words.

Key Components

    Text Parsing: The program reads a text file (corpus) and processes it to remove punctuation, numbers, and case sensitivity. The text is then split into sentences, with each sentence beginning with a special start token <s> and ending with an end token </s>.

    N-Gram Model Creation: The n-gram model is constructed by analyzing the corpus to count the occurrences of word sequences and then converting these counts into probabilities. This allows the model to predict the likelihood of a word following a given history of previous words.

    Sentence Prediction: Using the generated n-gram model, the program can generate new sentences by predicting the next word iteratively until a complete sentence is formed or a maximum length is reached.

    Backoff Mechanism: For higher-order n-grams (e.g., trigrams), if the model lacks data to predict the next word, it can "back off" to a lower-order model (e.g., bigram or unigram) to make a prediction, ensuring that the sentence generation process remains robust.

Running the Code

To run the code, you need to have a text corpus file (e.g., abc_corpus.txt). The program will prompt you to select the type of n-gram model (unigram, bigram, or trigram), the number of sentences to generate, and the maximum length of each sentence. The generated sentences will be saved in a text file.
Testing

Basic unit tests are included to verify the correctness of the text parsing and model creation functions. These tests help ensure that the n-gram model behaves as expected.
Conclusion

This project serves as a hands-on introduction to n-gram models, a fundamental concept in NLP that underpins more complex language models and applications.
