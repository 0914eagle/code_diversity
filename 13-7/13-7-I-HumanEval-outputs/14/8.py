
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    if not lst:
        return lst

    sorted_lst = []
    while lst:
        min_val = min(lst)
        max_val = max(lst)
        sorted_lst.append(min_val)
        sorted_lst.append(max_val)
        lst.remove(min_val)
        lst.remove(max_val)

    return sorted_lst

