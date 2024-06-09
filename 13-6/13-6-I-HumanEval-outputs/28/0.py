
from typing import List

def select_words(s: str, n: int) -> List[str]:
    
    words = s.split()
    result = []
    for word in words:
        count = 0
        for char in word:
            if char.isalpha() and char.islower():
                count += 1
        if count == n:
            result.append(word)
    return result

