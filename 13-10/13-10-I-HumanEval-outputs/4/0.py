
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    
    letter_counts: Dict[str, int] = {}
    for letter in test.split():
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
    most_frequent_letters = []
    max_count = 0
    for letter, count in letter_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_letters = [letter]
        elif count == max_count:
            most_frequent_letters.append(letter)
    return {letter: max_count for letter in most_frequent_letters}

