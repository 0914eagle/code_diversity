
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    if not arr:
        return True
    
    sorted_arr = sorted(arr)
    count = 0
    
    while arr != sorted_arr:
        if arr[-1] == sorted_arr[0]:
            arr.insert(0, arr.pop())
        else:
            arr.append(arr.pop(0))
        count += 1
        if count == len(arr):
            return False
    return True

