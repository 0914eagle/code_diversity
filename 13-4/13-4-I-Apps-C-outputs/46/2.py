
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
                # Check if the letter at position i is the first or last letter of the word
                if i == 0 or i == len(word) - 1:
                    # If it is, add it to the deciphered word as is
                    deciphered_word += word[i]
                else:
                    # If it is not, find the position of the letter in the word
                    pos = word.find(word[i])
                    # Add the letter to the deciphered word at the position it would be in if the word were sorted alphabetically
                    deciphered_word = deciphered_word[:pos] + word[i] + deciphered_word[pos:]
            # Add the deciphered word to the list of deciphered words
            deciphered_words.append(deciphered_word)
    
    # Join the deciphered words together to form the deciphered sentence
    deciphered_sentence = " ".join(deciphered_words)
    
    # Check if the deciphered sentence is unique
    if len(set(deciphered_sentence.split())) == len(deciphered_sentence.split()):
        # If it is unique, return the deciphered sentence
        return deciphered_sentence
    else:
        # If it is not unique, return "ambiguous"
        return "ambiguous"

s = "tihssnetnceemkaesprfecetsesne"
n = 5
dictionary = ["makes", "perfect", "sense", "sentence", "this"]
print(decipher_sentence(s, n, dictionary))

