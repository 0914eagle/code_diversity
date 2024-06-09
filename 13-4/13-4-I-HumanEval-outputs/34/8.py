
from typing import List

def sort_array(array: List[int]) -> List[int]:
    
    # Check if the array is empty
    if not array:
        return array

    # Calculate the sum of the first and last index values
    first_index_value = array[0]
    last_index_value = array[-1]
    sum_first_last = first_index_value + last_index_value

    # Check if the sum is odd or even
    if sum_first_last % 2 == 0:
        # Even sum, sort in descending order
        return sorted(array, reverse=True)
    else:
        # Odd sum, sort in ascending order
        return sorted(array)

