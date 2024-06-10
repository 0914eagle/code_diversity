
from typing import List

def can_arrange(arr: List[int]) -> int:
    
    # sort the array in non-decreasing order
    arr.sort()
    # initialize the largest index to be returned
    largest_index = -1
    # loop through the array and find the largest index of an element which
    # is not greater than or equal to the element immediately preceding it
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            largest_index = i
    return largest_index

