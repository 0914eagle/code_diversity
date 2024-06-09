
from typing import List

def get_odd_collatz(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    odd_numbers = []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n % 2 == 1:
            odd_numbers.append(n)
    
    return sorted(odd_numbers)

