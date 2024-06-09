
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    if not s:
        return []
    
    words = s.split()
    result = []
    for word in words:
        if len([c for c in word if c.isconsonant()]) == n:
            result.append(word)
    return result

