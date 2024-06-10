
from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    
    # Initialize even and odd counters to 0
    even_count, odd_count = 0, 0

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Check if the number is a palindrome
        if str(i) == str(i)[::-1]:
            # Increment the appropriate counter
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    # Return a tuple with the count of even and odd palindromes
    return even_count, odd_count

