
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    # Initialize an empty list to store the sorted even indices
    sorted_even = []
    # Iterate over the input list
    for i, elem in enumerate(l):
        # If the index is even, append the element to the sorted even list
        if i % 2 == 0:
            sorted_even.append(elem)
    # Sort the sorted even list
    sorted_even.sort()
    # Initialize an empty list to store the output list
    output = []
    # Iterate over the input list again
    for i, elem in enumerate(l):
        # If the index is odd, append the element to the output list
        if i % 2 == 1:
            output.append(elem)
        # If the index is even, append the corresponding element from the sorted even list
        else:
            output.append(sorted_even.pop(0))
    return output

