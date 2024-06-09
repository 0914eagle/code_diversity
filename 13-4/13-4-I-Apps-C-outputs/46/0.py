
import re

def decipher_sentence(s, n, dictionary):
    # Initialize a list to store the deciphered words
    deciphered_words = []
    
    # Split the sentence into individual words
    words = s.split()
    
    # Loop through each word in the sentence
    for word in words:
        # Check if the word is in the dictionary
        if word in dictionary:
            # If the word is in the dictionary, add it to the list of deciphered words
            deciphered_words.append(word)
        else:
            # If the word is not in the dictionary, try to decipher it by rearranging the letters
            deciphered_word = ""
            for i in range(len(word)):
                # Skip the first and last letters of the word
                if i == 0 or i == len(word) - 1:
                    deciphered_word += word[i]
                else:
                    # Rearrange the letters of the word
                    deciphered_word += word[len(word) - 1 - i]
            # Check if the deciphered word is in the dictionary
            if deciphered_word in dictionary:
                # If the deciphered word is in the dictionary, add it to the list of deciphered words
                deciphered_words.append(deciphered_word)
            else:
                # If the deciphered word is not in the dictionary, the sentence is impossible to decipher
                return "impossible"
    
    # If all words in the sentence are deciphered, return the deciphered sentence
    if len(deciphered_words) == len(words):
        return " ".join(deciphered_words)
    # If not all words in the sentence are deciphered, the sentence is ambiguous
    else:
        return "ambiguous"

