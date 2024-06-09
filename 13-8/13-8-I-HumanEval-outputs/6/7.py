
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    # Sort the array in ascending order
    arr.sort()
    # Initialize the largest index to -1
    largest_index = -1
    # Iterate over the array
    for i in range(len(arr) - 1):
        # Check if the current element is less than or equal to the next element
        if arr[i] <= arr[i + 1]:
            # If it is, update the largest index
            largest_index = i
    # Return the largest index
    return largest_index

