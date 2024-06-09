
from typing import List

def add(lst: List[int]) -> int:
    
    # Initialize a sum variable to store the result
    sum = 0
    # Iterate through the list and add the even elements at odd indices
    for i in range(1, len(lst), 2):
        sum += lst[i]
    # Return the sum
    return sum

