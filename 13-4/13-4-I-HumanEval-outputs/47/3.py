
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    # Check if the array is empty
    if not arr:
        return True
    
    # Check if the array is already sorted in non-decreasing order
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        return True
    
    # Perform right shift operation and check if the array is sorted in non-decreasing order
    for i in range(len(arr)):
        arr.append(arr.pop(0))
        if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
            return True
    
    # If the array is not sorted in non-decreasing order after performing right shift operation, return False
    return False

