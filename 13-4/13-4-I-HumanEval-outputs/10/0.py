
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    if not lst:
        return []

    result = []
    while lst:
        minimum = min(lst)
        result.append(minimum)
        lst.remove(minimum)
        if lst:
            maximum = max(lst)
            result.append(maximum)
            lst.remove(maximum)

    return result

