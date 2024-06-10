
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    # Create a copy of the list to avoid modifying the original list
    lst_copy = lst.copy()
    result = []

    # While there are still elements in the list
    while lst_copy:
        # Find the minimum value in the list
        min_val = min(lst_copy)
        # Remove the minimum value from the list
        lst_copy.remove(min_val)
        # Add the minimum value to the result list
        result.append(min_val)
        # If there are still elements in the list
        if lst_copy:
            # Find the maximum value in the list
            max_val = max(lst_copy)
            # Remove the maximum value from the list
            lst_copy.remove(max_val)
            # Add the maximum value to the result list
            result.append(max_val)

    return result

