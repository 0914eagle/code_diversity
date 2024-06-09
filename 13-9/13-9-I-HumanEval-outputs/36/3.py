
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    # Initialize an empty list to store the words with n consonants
    words_with_n_consonants = []
    
    # Split the input string into a list of words using the split() method
    words = s.split()
    
    # Iterate through the list of words
    for word in words:
        # Count the number of consonants in the current word
        consonant_count = 0
        for char in word:
            if char.lower() not in "aeiou":
                consonant_count += 1
        
        # If the current word has exactly n consonants, add it to the list of words with n consonants
        if consonant_count == n:
            words_with_n_consonants.append(word)
    
    # Return the list of words with n consonants
    return words_with_n_consonants

