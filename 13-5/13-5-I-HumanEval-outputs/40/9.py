
from typing import List

def add(lst: List[int]) -> int:
    
    # Initialize a variable to store the sum
    sum = 0
    # Iterate over the list
    for i, x in enumerate(lst):
        # Check if the current element is even and the index is odd
        if x % 2 == 0 and i % 2 == 1:
            # Add the current element to the sum
            sum += x
    # Return the sum
    return sum

