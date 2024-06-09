
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    words = s.split()
    result = []
    for word in words:
        if word.count("b") == n:
            result.append(word)
    return result

