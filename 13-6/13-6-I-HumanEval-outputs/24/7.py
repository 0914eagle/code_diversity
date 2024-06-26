
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

    product = 1
    for s in signs:
        product *= s

    return sum(abs(x) for x in arr) * product

