
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    # Check if the list is empty
    if not lst:
        return lst

    # Find the minimum and maximum values in the list
    min_val = min(lst)
    max_val = max(lst)

    # Create a new list to store the result
    result = []

    # Add the minimum value to the result list
    result.append(min_val)

    # Create a copy of the list without the minimum value
    remaining_lst = lst.copy()
    remaining_lst.remove(min_val)

    # Add the maximum value from the remaining list to the result list
    result.append(max(remaining_lst))

    # Add the minimum value to the result list again
    result.append(min_val)

    # Return the result list
    return result
