
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    # Check if the input list is empty
    if not lst:
        return []

    # Find the minimum and maximum values in the list
    min_val = min(lst)
    max_val = max(lst)

    # Create a new list to store the result
    result = []

    # Add the minimum value to the result list
    result.append(min_val)

    # Add the maximum value to the result list
    result.append(max_val)

    # Add the minimum value again to the result list
    result.append(min_val)

    # Return the result list
    return result

