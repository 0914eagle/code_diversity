
from typing import List

def solution(lst: List[int]) -> int:
    
    # Initialize a variable to store the sum
    sum_odd_even = 0
    
    # Iterate through the list
    for i, num in enumerate(lst):
        # Check if the current element is odd and the index is even
        if num % 2 == 1 and i % 2 == 0:
            # Add the current element to the sum
            sum_odd_even += num
    
    # Return the sum
    return sum_odd_even

