
from typing import List

def make_a_pile(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("n must be a positive integer")

    pile = [n]
    while len(pile) < n:
        if pile[-1] % 2 == 0:
            pile.append(pile[-1] + 1)
        else:
            pile.append(pile[-1] + 2)

    return pile

