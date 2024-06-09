
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    # Initialize an empty list to store the sorted even indices
    sorted_even = []
    # Iterate over the even indices of the input list
    for i in range(0, len(l), 2):
        # Add the value at the current even index to the sorted list
        sorted_even.append(l[i])
    # Sort the sorted list
    sorted_even.sort()
    # Initialize an empty list to store the output list
    output = []
    # Iterate over the input list
    for i, value in enumerate(l):
        # If the current index is odd, add the value to the output list
        if i % 2 == 1:
            output.append(value)
        # Otherwise, add the next value from the sorted list to the output list
        else:
            output.append(sorted_even.pop(0))
    return output

