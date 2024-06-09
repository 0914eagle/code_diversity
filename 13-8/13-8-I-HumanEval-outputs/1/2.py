
from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    
    even_palindromes = 0
    odd_palindromes = 0

    for i in range(1, n+1):
        rev = int(str(i)[::-1])
        if i == rev:
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    return even_palindromes, odd_palindromes

