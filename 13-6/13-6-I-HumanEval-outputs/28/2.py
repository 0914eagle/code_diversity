
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    # Initialize an empty list to store the words
    words: List[str] = []
    
    # Split the input string into a list of words using split()
    words_list = s.split()
    
    # Iterate over the list of words
    for word in words_list:
        # Check if the word contains exactly n consonants
        if len([letter for letter in word if letter.isalpha() and not letter.isalpha()]) == n:
            # If the word contains exactly n consonants, add it to the list of words
            words.append(word)
    
    # Return the list of words
    return words

