
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    # Sort the even indices of the list
    sorted_evens = sorted(l[1::2])
    # Create a new list with the same odd indices as the input list
    sorted_list = [l[i] for i in range(len(l)) if i % 2 == 0]
    # Add the sorted even indices to the new list
    sorted_list.extend(sorted_evens)
    return sorted_list

