
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    
    # Your code here
    letter_count = {}
    for letter in test.split():
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    
    max_count = max(letter_count.values())
    return {k: v for k, v in letter_count.items() if v == max_count}
