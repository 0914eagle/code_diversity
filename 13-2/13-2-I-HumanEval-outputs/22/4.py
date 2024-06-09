
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    
    letter_counts: Dict[str, int] = {}
    for letter in test.split():
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    
    max_count = max(letter_counts.values())
    most_frequent_letters = [letter for letter, count in letter_counts.items() if count == max_count]
    
    return {letter: max_count for letter in most_frequent_letters}

