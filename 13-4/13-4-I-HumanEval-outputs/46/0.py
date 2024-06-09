
from typing import List

def add(lst: List[int]) -> int:
    
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the list
    for i, num in enumerate(lst):
        # Check if the current index is odd and the current number is even
        if i % 2 == 1 and num % 2 == 0:
            # Add the current number to the sum
            sum += num
    # Return the sum
    return sum

