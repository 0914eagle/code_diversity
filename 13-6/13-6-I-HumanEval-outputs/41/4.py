
from typing import List

def add(lst: List[int]) -> int:
    
    # Initialize the sum variable
    sum = 0
    # Iterate over the list and add the even elements at odd indices
    for i in range(1, len(lst), 2):
        sum += lst[i]
    # Return the sum
    return sum

