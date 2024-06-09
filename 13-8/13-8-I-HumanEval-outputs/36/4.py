
from typing import List

def add_elements(arr: List[int], k: int) -> int:
    
    # Initialize a variable to store the sum
    sum_ = 0
    # Iterate through the first k elements of the array
    for i in range(k):
        # Check if the element has at most two digits
        if len(str(arr[i])) <= 2:
            # Add the element to the sum
            sum_ += arr[i]
    # Return the sum
    return sum_

