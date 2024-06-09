
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    # Initialize an empty list to store the sorted even values
    sorted_even_values = []

    # Iterate over the even indicies of the list
    for i in range(0, len(l), 2):
        # Add the current value at the even index to the sorted list
        sorted_even_values.append(l[i])

    # Sort the sorted list of even values
    sorted_even_values.sort()

    # Initialize an empty list to store the sorted list
    sorted_list = []

    # Iterate over the original list
    for i in range(len(l)):
        # If the current index is odd, add the current value to the sorted list
        if i % 2 == 1:
            sorted_list.append(l[i])
        # Otherwise, add the current sorted even value to the sorted list
        else:
            sorted_list.append(sorted_even_values[i // 2])

    return sorted_list

