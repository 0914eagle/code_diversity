
from typing import List

def sort_array(array: List[int]) -> List[int]:
    
    # Check if the array is empty
    if not array:
        return array

    # Get the sum of the first and last elements
    first_last_sum = array[0] + array[-1]

    # Check if the sum is odd or even
    if first_last_sum % 2 == 0:
        # Sort the array in descending order
        return sorted(array, reverse=True)
    else:
        # Sort the array in ascending order
        return sorted(array)

