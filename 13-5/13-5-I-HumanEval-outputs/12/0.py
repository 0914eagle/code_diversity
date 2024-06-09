
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    # Initialize an empty list to store the sorted even indices
    sorted_even_indices = []

    # Iterate through the list and append the even indices to the sorted list
    for i in range(0, len(l), 2):
        sorted_even_indices.append(l[i])

    # Sort the sorted list
    sorted_even_indices.sort()

    # Initialize an empty list to store the sorted list with the original odd indices
    sorted_list = []

    # Iterate through the list and append the sorted even indices to the sorted list
    for i in range(len(l)):
        if i % 2 == 0:
            sorted_list.append(sorted_even_indices[i // 2])
        else:
            sorted_list.append(l[i])

    return sorted_list

