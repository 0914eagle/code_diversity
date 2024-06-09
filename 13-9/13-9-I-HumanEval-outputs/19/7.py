
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    # Initialize an empty list to store the sorted even indices
    sorted_evens = []
    # Iterate through the even indices of the input list
    for i in range(0, len(l), 2):
        # Add the current value at the even index to the sorted list
        sorted_evens.append(l[i])
    # Sort the sorted list
    sorted_evens.sort()
    # Initialize an empty list to store the output
    output = []
    # Iterate through the input list
    for i in range(len(l)):
        # If the current index is odd, add the current value to the output list
        if i % 2 == 1:
            output.append(l[i])
        # Otherwise, add the corresponding value from the sorted list to the output list
        else:
            output.append(sorted_evens[i // 2])
    return output

