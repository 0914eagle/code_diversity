
from typing import List

def add_elements(arr: List[int], k: int) -> int:
    
    # Initialize a variable to store the sum
    sum_elements = 0

    # Iterate through the first k elements of the array
    for i in range(k):
        # Get the current element
        element = arr[i]

        # Check if the element has at most two digits
        if len(str(element)) <= 2:
            # If it does, add it to the sum
            sum_elements += element

    # Return the sum
    return sum_elements

