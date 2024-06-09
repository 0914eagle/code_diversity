
from typing import List

def solution(lst: List[int]) -> int:
    
    # Initialize a variable to store the sum
    sum_odd_even = 0
    
    # Iterate through the list
    for i, num in enumerate(lst):
        # Check if the number is odd and the index is even
        if num % 2 != 0 and i % 2 == 0:
            # Add the number to the sum
            sum_odd_even += num
    
    # Return the sum
    return sum_odd_even

