
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    n = len(arr)
    if n == 1:
        return -1

    # find the maximum element in the array
    max_element = max(arr)

    # find the index of the maximum element
    max_index = arr.index(max_element)

    # check if the element to the left of the maximum element is less than or equal to it
    if max_index > 0 and arr[max_index - 1] <= max_element:
        return max_index - 1

    # if the element to the left of the maximum element is greater than it, then return -1
    return -1

