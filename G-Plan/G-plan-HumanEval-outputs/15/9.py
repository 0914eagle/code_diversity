
from typing import List
import re

def count_consonants(word: str) -> int:
    return sum(1 for letter in word if letter.lower() not in 'aeiou' and letter.isalpha())

def select_words(s: str, n: int) -> List[str]:
    words = s.split()
    pattern = r'\b(?:[a-zA-Z]*[^aeiou]){'+str(n)+r'}[a-zA-Z]*\b'
    return re.findall(pattern, s)

s, n = input().split(', ')
n = int(n)
result = select_words(s, n)
print(result)
