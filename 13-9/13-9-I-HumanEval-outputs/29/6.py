
from typing import List

def get_odd_collatz(n: int) -> List[int]:
    
    if n < 1:
        raise ValueError("n must be a positive integer")

    collatz = []
    current = n
    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = current * 3 + 1
        if current not in collatz:
            collatz.append(current)

    return sorted(collatz)

