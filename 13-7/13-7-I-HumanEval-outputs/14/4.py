
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    if not lst:
        return lst

    result = []
    while lst:
        minimum = min(lst)
        result.append(minimum)
        lst.remove(minimum)
        maximum = max(lst)
        result.append(maximum)
        lst.remove(maximum)

    return result

