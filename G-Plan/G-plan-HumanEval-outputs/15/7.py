
from typing import List

def count_consonants(word: str) -> int:
    return sum(1 for letter in word if letter.lower() not in 'aeiou' and letter.isalpha())

def select_words(s: str, n: int) -> List[str]:
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result

# Input parsing
input_string, n = input().split(', ')
n = int(n)
print(select_words(input_string, n))
