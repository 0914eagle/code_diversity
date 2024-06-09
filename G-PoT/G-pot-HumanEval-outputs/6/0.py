
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    sum_first_last = array[0] + array[-1]
    sorted_array = array.copy()

    if sum_first_last % 2 == 1:
        sorted_array.sort()
    else:
        sorted_array.sort(reverse=True)

    return sorted_array
