
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    
    hist: Dict[str, int] = {}
    for letter in test.split():
        if letter not in hist:
            hist[letter] = 1
        else:
            hist[letter] += 1
    return hist

