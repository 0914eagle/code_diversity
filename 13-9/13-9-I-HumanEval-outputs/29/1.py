
from typing import List

def get_odd_collatz(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    collatz_sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_sequence.append(n)

    return sorted([x for x in collatz_sequence if x % 2 == 1])

