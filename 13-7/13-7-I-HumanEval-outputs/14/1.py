
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    # Check if the input list is empty
    if not lst:
        return lst

    # Find the minimum and maximum values in the list
    min_val = min(lst)
    max_val = max(lst)

    # Create a new list to store the sorted values
    sorted_lst = []

    # Add the minimum value to the sorted list
    sorted_lst.append(min_val)

    # Add the maximum value to the sorted list
    sorted_lst.append(max_val)

    # Remove the minimum and maximum values from the original list
    lst.remove(min_val)
    lst.remove(max_val)

    # Repeat the process of finding the minimum and maximum values
    # and adding them to the sorted list until the original list is empty
    while lst:
        min_val = min(lst)
        max_val = max(lst)
        sorted_lst.append(min_val)
        sorted_lst.append(max_val)
        lst.remove(min_val)
        lst.remove(max_val)

    return sorted_lst

