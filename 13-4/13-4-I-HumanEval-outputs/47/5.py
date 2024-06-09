
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    if not arr:
        return True
    
    # check if the array is sorted in non-decreasing order
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        return True
    
    # perform right shift operation and check if the array is sorted in non-decreasing order
    for i in range(len(arr)):
        arr.append(arr.pop(0))
        if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
            return True
    
    return False

