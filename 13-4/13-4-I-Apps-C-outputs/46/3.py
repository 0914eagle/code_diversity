
import re

def decipher_sentence(s, n, dictionary):
    # Initialize a list to store the deciphered words
    deciphered_words = []

    # Iterate through each word in the dictionary
    for word in dictionary:
        # Check if the word is a substring of the sentence
        if word in s:
            # If the word is a substring, add it to the list of deciphered words
            deciphered_words.append(word)

            # Remove the word from the sentence
            s = s.replace(word, "")

    # If the sentence is empty, return the list of deciphered words
    if s == "":
        return " ".join(deciphered_words)

    # If the sentence is not empty, check if it can be deciphered uniquely
    unique_deciphered_words = []
    for word in deciphered_words:
        # Check if the word is a substring of the sentence
        if word in s:
            # If the word is a substring, add it to the list of unique deciphered words
            unique_deciphered_words.append(word)

            # Remove the word from the sentence
            s = s.replace(word, "")

    # If the list of unique deciphered words is not empty, return it
    if unique_deciphered_words:
        return " ".join(unique_deciphered_words)

    # If the list of unique deciphered words is empty, return "impossible"
    return "impossible"

