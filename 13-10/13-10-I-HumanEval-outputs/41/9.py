
from typing import List

def make_a_pile(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("n must be a positive integer")

    pile = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        pile.append(n)

    return pile

