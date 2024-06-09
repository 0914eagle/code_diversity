
from typing import List

def solution(lst: List[int]) -> int:
    
    # Initialize a variable to store the sum
    sum_of_odd_elements = 0
    
    # Iterate through the list
    for i, element in enumerate(lst):
        # Check if the element is odd and the index is even
        if element % 2 == 1 and i % 2 == 0:
            # Add the element to the sum
            sum_of_odd_elements += element
    
    # Return the sum
    return sum_of_odd_elements

