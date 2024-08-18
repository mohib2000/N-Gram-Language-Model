import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import abc

# This function processes and cleans individual words
def clean_word(word):
    # Lowercase and remove non-alphabetic characters
    return "".join([char.lower() for char in word if char.isalpha()])

# This function handles contractions and returns expanded form
def handle_contractions(word, next_word):
    contractions = {"'m": "am", "'s": "is", "'re": "are", "'ve": "have", "'d": "would",
                    "'ll": "will", "n't": "not"}
    return contractions.get(next_word, next_word)

nltk.download('punkt')

# Initialize list for processed sentences
sentences = []
for s in abc.sents():
    processed_sentence = []
    i = 0
    while i < len(s):
        word = s[i]

        if i + 1 < len(s) and s[i + 1] in ["'m", "'s", "'re", "'ve", "'d", "'ll", "n't"]:
            # Handle contractions
            processed_word = clean_word(word)
            processed_sentence.append(processed_word)
            processed_sentence.append(handle_contractions(word, s[i + 1]))
            i += 2  # Skip the next word as it's part of the contraction
        else:
            processed_word = clean_word(word)
            if processed_word:  # Add non-empty words
                processed_sentence.append(processed_word)
            i += 1

    final_sentence = " ".join(processed_sentence) + "."
    sentences.append(final_sentence)

# Write processed sentences to file
with open("abc_corpus.txt", 'w') as f:
    f.write("\n".join(sentences))
