
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    if not s:
        return []
    
    words = s.split()
    result = []
    for word in words:
        if len([letter for letter in word if letter.isalpha() and not letter.isalpha()]) == n:
            result.append(word)
    return result

