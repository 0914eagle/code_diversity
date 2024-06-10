
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    if not lst:
        return []

    result = []
    while lst:
        # find the minimum element
        min_index = lst.index(min(lst))
        result.append(lst[min_index])
        # remove the minimum element
        lst.pop(min_index)

        # find the maximum element among the remaining elements
        max_index = lst.index(max(lst))
        result.append(lst[max_index])
        # remove the maximum element
        lst.pop(max_index)

    return result

