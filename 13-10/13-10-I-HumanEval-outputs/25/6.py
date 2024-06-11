
from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    
    num = abs(num)
    even_digits = 0
    odd_digits = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
        num //= 10
    return even_digits, odd_digits
