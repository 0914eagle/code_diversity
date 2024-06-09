
from typing import List

def pluck(arr: List[int]) -> List[int]:
    
    # Find the smallest even value in the array
    smallest_even = float('inf')
    for i, node in enumerate(arr):
        if node % 2 == 0 and node < smallest_even:
            smallest_even = node
            smallest_even_index = i

    # If there are no even values or the array is empty, return an empty list
    if smallest_even == float('inf') or smallest_even == 0:
        return []

    # Return the smallest even value and its index
    return [smallest_even, smallest_even_index]

