
from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    
    even_palindromes = 0
    odd_palindromes = 0

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Check if the number is a palindrome
        if str(i) == str(i)[::-1]:
            # Increment the appropriate counter
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    return even_palindromes, odd_palindromes

