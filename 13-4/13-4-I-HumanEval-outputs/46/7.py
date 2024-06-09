
from typing import List

def add(lst: List[int]) -> int:
    
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the list
    for i, element in enumerate(lst):
        # Check if the element is even and the index is odd
        if element % 2 == 0 and i % 2 == 1:
            # Add the element to the sum
            sum += element
    # Return the sum
    return sum

