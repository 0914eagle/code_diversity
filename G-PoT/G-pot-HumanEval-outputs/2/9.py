
from typing import List

def find_max(words: List[str]) -> str:
    unique_chars = lambda word: len(set(word))
    max_unique = max(words, key=lambda word: (unique_chars(word), word))
    return max_unique
