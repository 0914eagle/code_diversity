
from typing import List

def make_a_pile(n: int) -> List[int]:
    
    if n <= 0:
        return []

    levels = []
    while n > 0:
        levels.append(n)
        n = n // 2 if n % 2 == 0 else n // 2 + 1

    return levels[::-1]

