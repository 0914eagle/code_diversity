
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    if not arr:
        return True
    
    # convert the array to a set to remove duplicates
    unique_elements = set(arr)
    if len(unique_elements) != len(arr):
        return False
    
    # sort the array in non-decreasing order
    arr.sort()
    
    # check if the array is sorted in non-decreasing order
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    
    return True

