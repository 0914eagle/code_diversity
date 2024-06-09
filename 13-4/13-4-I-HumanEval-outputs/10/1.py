
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    if not lst:
        return lst

    sorted_lst = sorted(lst)
    result = [sorted_lst[0]]
    for i in range(1, len(lst)):
        if sorted_lst[i] not in result:
            result.append(sorted_lst[i])

    return result

