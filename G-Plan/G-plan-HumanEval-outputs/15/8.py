
from typing import List
import re

def count_consonants(word: str) -> int:
    return sum(1 for letter in word if letter.lower() not in 'aeiou' and letter.isalpha())

def select_words(s: str, n: int) -> List[str]:
    if not s:
        return []

    words = s.split()
    pattern = r"\b(?:[a-zA-Z]*[^aeiou]){%d}[a-zA-Z]*\b" % n
    return [word for word in words if re.match(pattern, word)]

s, n = input().split(', ')
n = int(n)
result = select_words(s, n)
print(result)
