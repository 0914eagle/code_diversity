
from typing import List

def make_a_pile(n: int) -> List[int]:
    
    if n < 1:
        raise ValueError("n must be a positive integer")

    levels = []
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        levels.append(n)

    return levels[::-1]

