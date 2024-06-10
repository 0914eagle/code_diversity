
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    # Check if the input array is empty
    if not arr:
        return True
    
    # Sort the input array
    arr.sort()
    
    # Check if the array is sorted in non-decreasing order
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    
    return True

