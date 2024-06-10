
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    if not lst:
        return []
    sorted_list = []
    while lst:
        sorted_list.append(min(lst))
        lst.remove(min(lst))
        if lst:
            sorted_list.append(max(lst))
            lst.remove(max(lst))
    return sorted_list

