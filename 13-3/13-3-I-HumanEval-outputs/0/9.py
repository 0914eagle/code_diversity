
from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    
    if not arr:
        return None

    signs = [1 for _ in arr]
    for i, num in enumerate(arr):
        if num == 0:
            signs[i] = 0
        elif num < 0:
            signs[i] = -1

    prod = 1
    for sign in signs:
        prod *= sign

    return sum(arr) * prod

