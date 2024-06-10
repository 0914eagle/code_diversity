
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    # Sort the array in ascending order
    arr.sort()

    # Initialize the largest index to be returned
    largest_index = -1

    # Iterate through the array and find the largest index where the element is
    # not greater than or equal to the element immediately preceding it
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            largest_index = i

    return largest_index

