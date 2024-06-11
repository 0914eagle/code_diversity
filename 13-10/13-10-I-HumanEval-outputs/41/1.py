
from typing import List

def make_a_pile(n: int) -> List[int]:
    
    levels = []
    while n > 0:
        levels.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return levels[::-1]
