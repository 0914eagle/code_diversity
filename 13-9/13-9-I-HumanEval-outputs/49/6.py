
from typing import List

def find_max(words: List[str]) -> str:
    
    max_word = ""
    max_unique_chars = 0
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_unique_chars:
            max_word = word
            max_unique_chars = len(unique_chars)
    return max_word

