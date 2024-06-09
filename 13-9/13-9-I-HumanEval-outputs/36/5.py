
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    words = []
    for word in s.split():
        if len([c for c in word if c.isalpha() and not c.isalpha()]) == n:
            words.append(word)
    return words

