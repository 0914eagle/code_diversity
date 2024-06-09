
from typing import List

def pluck(arr: List[int]) -> List[int]:
    
    # Find the smallest even value in the array
    smallest_even = float('inf')
    for i, node in enumerate(arr):
        if node % 2 == 0 and node < smallest_even:
            smallest_even = node
            smallest_index = i

    # If there are no even values or the array is empty, return []
    if smallest_even == float('inf'):
        return []

    # Return the node with the smallest even value and its index
    return [smallest_even, smallest_index]

