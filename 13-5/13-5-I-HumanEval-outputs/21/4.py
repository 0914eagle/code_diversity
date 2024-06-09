
from typing import List

def solution(lst: List[int]) -> int:
    
    # Initialize a variable to store the sum
    sum_odd_even = 0
    
    # Iterate through the list
    for i, element in enumerate(lst):
        # Check if the element is odd and the index is even
        if element % 2 != 0 and i % 2 == 0:
            # Add the element to the sum
            sum_odd_even += element
    
    # Return the sum
    return sum_odd_even

