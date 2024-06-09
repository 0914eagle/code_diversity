
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    # find the maximum value in the array
    max_val = max(arr)

    # iterate through the array and find the largest index of an element that is not greater than or equal to the element immediately preceding it
    for i in range(len(arr) - 1):
        if arr[i] < arr[i+1]:
            continue
        elif arr[i] >= arr[i+1]:
            return i

    # if no such element exists, return -1
    return -1

