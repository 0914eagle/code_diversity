
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    # Find the maximum element in the array
    max_element = max(arr)

    # Initialize a variable to store the largest index of an element that is not greater than or equal to the element immediately preceding it
    largest_index = -1

    # Iterate over the array
    for i in range(len(arr) - 1):
        # If the current element is less than the maximum element and the element immediately preceding it is greater than or equal to the maximum element
        if arr[i] < max_element and arr[i + 1] >= max_element:
            # Update the largest index
            largest_index = i

    # Return the largest index
    return largest_index

