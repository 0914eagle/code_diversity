
from typing import List

def find_max(words: List[str]) -> str:
    

    max_word = ""
    max_unique_chars = 0

    for word in words:
        unique_chars = set()
        for char in word:
            if char not in unique_chars:
                unique_chars.add(char)
        if len(unique_chars) > max_unique_chars:
            max_unique_chars = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_unique_chars:
            if word < max_word:
                max_word = word

    return max_word

