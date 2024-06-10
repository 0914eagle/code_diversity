
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    
    # Your code here
    hist = {}
    for char in test.split(' '):
        if char not in hist:
            hist[char] = 1
        else:
            hist[char] += 1
    
    max_count = max(hist.values())
    max_letters = [letter for letter, count in hist.items() if count == max_count]
    
    return dict(zip(max_letters, [max_count] * len(max_letters)))

