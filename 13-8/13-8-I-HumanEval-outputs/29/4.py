
from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    
    even_count = 0
    odd_count = 0

    while num != 0:
        digit = num % 10
        num //= 10

        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

