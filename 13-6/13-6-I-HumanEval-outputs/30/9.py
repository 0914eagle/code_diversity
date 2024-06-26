
from typing import List

def find_max(words: List[str]) -> str:
    
    max_word = ""
    max_unique_chars = 0
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars and word < max_word:
            max_word = word
    return max_word

