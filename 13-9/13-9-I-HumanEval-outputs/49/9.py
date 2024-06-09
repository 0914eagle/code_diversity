
from typing import List

def find_max(words: List[str]) -> str:
    
    max_word = ""
    max_count = 0
    for word in words:
        word_count = len(set(word))
        if word_count > max_count:
            max_count = word_count
            max_word = word
        elif word_count == max_count and word < max_word:
            max_word = word
    return max_word

