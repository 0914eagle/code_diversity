
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    sum_first_last = array[0] + array[-1]
    sorted_array = sorted(array)

    if sum_first_last % 2 == 0:
        return sorted_array[::-1]
    else:
        return sorted_array