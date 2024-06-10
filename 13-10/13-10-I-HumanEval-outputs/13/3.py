
from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    
    if not arr:
        return None

    signs = [1] * len(arr)
    for i in range(len(arr)):
        if arr[i] < 0:
            signs[i] = -1
        elif arr[i] == 0:
            signs[i] = 0

    product = 1
    for i in range(len(arr)):
        product *= signs[i]

    return sum(arr) * product

