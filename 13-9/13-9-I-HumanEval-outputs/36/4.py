
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    words = s.split()
    result = []
    for word in words:
        if len([char for char in word if char.isalpha() and char.lower() not in "aeiou"]) == n:
            result.append(word)
    return result

