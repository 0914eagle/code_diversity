
from typing import List

def count_consonants(word: str) -> int:
    vowels = 'aeiouAEIOU'
    return sum(1 for char in word if char.isalpha() and char not in vowels)

def select_words(s: str, n: int) -> List[str]:
    if not s:
        return []
    
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    
    return result

# Read input
s, n = input().strip().split(', ')
n = int(n)

# Call the function and print the result
print(select_words(s, n))
