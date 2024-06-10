
from typing import List
import re

def count_consonants(word: str) -> int:
    return sum(1 for letter in word if letter.lower() not in 'aeiou' and letter.isalpha())

def select_words(s: str, n: int) -> List[str]:
    words = s.split()
    pattern = r'\b(?:[a-zA-Z]*[^aeiou]){'+str(n)+'}[a-zA-Z]*\b'
    return [word for word in words if re.match(pattern, word)]

s, n = input().split(', ')
n = int(n)
print(select_words(s, n))
