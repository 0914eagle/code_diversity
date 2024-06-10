
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    
    letter_count = {}
    for letter in test.split():
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    
    max_count = max(letter_count.values())
    most_frequent_letters = [letter for letter, count in letter_count.items() if count == max_count]
    
    return {letter: max_count for letter in most_frequent_letters}

