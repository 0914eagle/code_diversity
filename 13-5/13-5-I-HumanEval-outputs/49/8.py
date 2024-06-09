
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    # Initialize a variable to store the largest index of an element that
    # is not greater than or equal to the element immediately preceding it
    largest_index = -1

    # Iterate over the array
    for i in range(len(arr) - 1):
        # Check if the current element is not greater than or equal to the
        # element immediately preceding it
        if arr[i] < arr[i + 1]:
            # If it is not, then update the largest index variable
            largest_index = i

    # Return the largest index
    return largest_index

