
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    # Initialize variables
    n = len(arr)
    largest_index = -1

    # Iterate through the array
    for i in range(n - 1):
        # Check if the current element is not greater than or equal to the element immediately preceding it
        if arr[i] < arr[i + 1]:
            # Update the largest index
            largest_index = i

    # Return the largest index
    return largest_index

