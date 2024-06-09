
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    # Your code here
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return i
    return -1

