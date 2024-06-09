
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    if not arr:
        return True
    
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            return False
    return True

