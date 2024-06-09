
from typing import List

def find_max(words: List[str]) -> str:
    
    def count_unique_chars(word):
        return len(set(word))

    max_word = ''
    max_unique_chars = 0

    for word in words:
        unique_chars = count_unique_chars(word)
        if unique_chars > max_unique_chars or (unique_chars == max_unique_chars and word < max_word):
            max_word = word
            max_unique_chars = unique_chars

    return max_word
