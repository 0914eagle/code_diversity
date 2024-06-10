
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    if len(arr) < 2:
        return -1

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= arr[i + 1]:
            return i

    return -1

