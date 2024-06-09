
from typing import List

def pluck(arr: List[int]) -> List[int]:
    
    # Find the smallest even value in the array
    smallest_even_value = float('inf')
    for i, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even_value:
            smallest_even_value = value
            smallest_even_index = i

    # If there are no even values or the given array is empty, return []
    if smallest_even_value == float('inf'):
        return []

    # Return the plucked node in a list, [smallest_even_value, smallest_even_index]
    return [smallest_even_value, smallest_even_index]

