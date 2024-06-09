
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    words = s.split()
    selected_words = []
    for word in words:
        if len([c for c in word if not c.isalpha()]) == n:
            selected_words.append(word)
    return selected_words

