
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    # Initialize an empty list to store the words with n consonants
    words_with_n_consonants = []
    
    # Split the input string into a list of words using the split() method
    words = s.split()
    
    # Iterate over the list of words
    for word in words:
        # Count the number of consonants in the current word
        num_consonants = 0
        for char in word:
            if char.lower() not in "aeiou":
                num_consonants += 1
        
        # If the number of consonants is equal to n, add the word to the list of words with n consonants
        if num_consonants == n:
            words_with_n_consonants.append(word)
    
    # Return the list of words with n consonants
    return words_with_n_consonants

