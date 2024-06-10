
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    if not lst:
        return []
    sorted_lst = sorted(lst)
    result = []
    while sorted_lst:
        result.append(sorted_lst[0])
        sorted_lst = sorted_lst[1:] + sorted_lst[:1]
    return result

