
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    # Initialize an empty list to store the selected words
    selected_words = []
    
    # Split the input string into a list of words using the split() method
    words = s.split()
    
    # Iterate over the list of words
    for word in words:
        # Count the number of consonants in the current word
        consonants = 0
        for char in word:
            if char.lower() not in "aeiou":
                consonants += 1
        
        # If the number of consonants is equal to n, add the word to the list of selected words
        if consonants == n:
            selected_words.append(word)
    
    # Return the list of selected words
    return selected_words

