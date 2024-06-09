
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    first_index = array[0]
    last_index = array[-1]
    total_sum = first_index + last_index

    if total_sum % 2 == 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)
