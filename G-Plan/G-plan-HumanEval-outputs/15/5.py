
from typing import List
import re

def count_consonants(word: str) -> int:
    return sum(1 for letter in word if letter.lower() not in 'aeiou')

def select_words(s: str, n: int) -> List[str]:
    words = s.split()
    pattern = r'\b[^aeiouAEIOU\s]{%d}\b' % n
    return [word for word in words if re.match(pattern, word)]

s, n = input().split(', ')
n = int(n)
result = select_words(s, n)
print(result)
