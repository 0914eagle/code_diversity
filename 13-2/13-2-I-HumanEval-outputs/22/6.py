
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    
    # Your code here
    hist = {}
    for char in test.split():
        if char not in hist:
            hist[char] = 1
        else:
            hist[char] += 1
    return hist

