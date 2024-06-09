
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return i
    return -1

