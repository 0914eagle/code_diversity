
from typing import List

def get_odd_collatz(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("n must be a positive integer")

    collatz_seq = []
    while n != 1:
        collatz_seq.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    odd_numbers = [x for x in collatz_seq if x % 2 != 0]
    return sorted(odd_numbers)

