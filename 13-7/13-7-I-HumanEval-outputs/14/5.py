
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    if len(lst) == 0:
        return []

    sorted_lst = sorted(lst)
    result = [sorted_lst[0]]

    for i in range(1, len(lst)):
        if lst[i] not in result:
            result.append(lst[i])

    return result

