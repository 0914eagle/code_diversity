
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    if not s:
        return []
    
    words = s.split()
    selected_words = []
    
    for word in words:
        if len([c for c in word if c.isalpha() and not c.isalpha()]) == n:
            selected_words.append(word)
    
    return selected_words

