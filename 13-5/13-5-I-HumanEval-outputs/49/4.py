
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    n = len(arr)
    if n == 1:
        return -1
    max_idx = -1
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            max_idx = i
    return max_idx

