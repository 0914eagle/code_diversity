
from typing import List

def pluck(arr: List[int]) -> List[int]:
    
    # Find the smallest even value in the array
    smallest_even_value = float('inf')
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_even_value:
            smallest_even_value = arr[i]

    # If there are no even values or the array is empty, return an empty list
    if smallest_even_value == float('inf') or len(arr) == 0:
        return []

    # Find the index of the smallest even value
    smallest_even_index = 0
    for i in range(len(arr)):
        if arr[i] == smallest_even_value:
            smallest_even_index = i
            break

    return [smallest_even_value, smallest_even_index]

