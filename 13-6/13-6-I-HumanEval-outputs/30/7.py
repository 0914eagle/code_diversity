
from typing import List

def find_max(words: List[str]) -> str:
    
    max_word = ""
    max_count = 0
    for word in words:
        unique_chars = set()
        for char in word:
            unique_chars.add(char)
        if len(unique_chars) > max_count:
            max_count = len(unique_chars)
            max_word = word
    return max_word

