
from typing import List

def make_a_pile(n: int) -> List[int]:
    
    if n <= 0:
        return []
    levels = [n]
    while len(levels) < n:
        if levels[-1] % 2 == 0:
            levels.append(levels[-1] + 1)
        else:
            levels.append(levels[-1] + 2)
    return levels

