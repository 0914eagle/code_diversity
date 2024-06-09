
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    n = len(arr)
    if n == 1:
        return -1
    else:
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return i
        return -1

