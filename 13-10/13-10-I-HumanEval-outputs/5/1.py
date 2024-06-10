
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    if not arr:
        return True
    
    sorted_arr = sorted(arr)
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    
    return True

