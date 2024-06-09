
from typing import List

def pluck(arr: List[int]) -> List[int]:
    
    # Find the smallest even value in the array
    even_values = [value for value in arr if value % 2 == 0]
    smallest_even_value = min(even_values, default=None)

    # If there are no even values, return an empty list
    if smallest_even_value is None:
        return []

    # Find the index of the smallest even value
    smallest_even_value_index = arr.index(smallest_even_value)

    # Return the smallest even value and its index
    return [smallest_even_value, smallest_even_value_index]

