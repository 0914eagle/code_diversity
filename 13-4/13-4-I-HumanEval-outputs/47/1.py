
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    if not arr:
        return True
    
    arr.sort()
    return arr == list(range(1, len(arr) + 1))

