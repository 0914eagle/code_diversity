
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    # Check if the array is empty
    if not arr:
        return True
    
    # Check if the array is already sorted in non-decreasing order
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        return True
    
    # Initialize a boolean variable to keep track of whether it is possible to get the sorted array
    possible = False
    
    # Perform right shift operations on the array until it is sorted in non-decreasing order or the array becomes empty
    while arr and not possible:
        # Right shift the array by one position
        arr.append(arr.pop(0))
        
        # Check if the array is sorted in non-decreasing order
        if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
            possible = True
            
    return possible

