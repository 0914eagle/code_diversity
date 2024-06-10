
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    if not arr:
        return True
    
    sorted_arr = sorted(arr)
    current_arr = arr.copy()
    
    while current_arr != sorted_arr:
        current_arr.append(current_arr.pop(0))
        if current_arr == sorted_arr:
            return True
    
    return False

