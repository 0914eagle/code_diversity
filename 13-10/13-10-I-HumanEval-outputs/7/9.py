
from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    
    return (sum(q) <= w) and (q == q[::-1])

