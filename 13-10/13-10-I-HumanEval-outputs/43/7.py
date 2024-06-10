
from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    
    even_count = 0
    odd_count = 0

    for i in range(1, n + 1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            even_count += 1
        elif str(i) == str(i)[::-1] and i % 2 == 1:
            odd_count += 1

    return even_count, odd_count

