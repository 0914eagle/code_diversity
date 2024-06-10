
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    # Your code here
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            return i
    return -1

