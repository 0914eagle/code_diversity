
from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    
    even_palindromes = 0
    odd_palindromes = 0

    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            even_palindromes += 1
        elif str(i) == str(i)[::-1] and i % 2 == 1:
            odd_palindromes += 1

    return even_palindromes, odd_palindromes

