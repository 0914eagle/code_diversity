
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    # Initialize an empty list to store the sorted values
    sorted_values = []

    # Iterate through the input list and extract the even indicies
    for i, value in enumerate(l):
        if i % 2 == 0:
            sorted_values.append(value)

    # Sort the extracted even indicies
    sorted_values.sort()

    # Create a new list with the sorted values at the even indicies
    sorted_list = []
    for i, value in enumerate(l):
        if i % 2 == 0:
            sorted_list.append(sorted_values[i // 2])
        else:
            sorted_list.append(value)

    return sorted_list

