
from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    
    if not arr:
        return None

    signs = [1 for _ in arr]
    for i, x in enumerate(arr):
        if x < 0:
            signs[i] = -1
        elif x == 0:
            signs[i] = 0

    prod = 1
    for x in signs:
        prod *= x

    return sum(arr) * prod

