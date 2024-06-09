
from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    
    if len(lst) == 0:
        return lst

    result = []
    while lst:
        result.append(min(lst))
        lst.remove(min(lst))
        if len(lst) > 0:
            result.append(max(lst))
            lst.remove(max(lst))

    return result

