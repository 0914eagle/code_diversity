
from typing import List

def is_sorted(lst: List[int]) -> bool:
    
    if len(lst) <= 1:
        return True

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
        if lst[i] == lst[i + 1]:
            if lst.count(lst[i]) > 1:
                return False

    return True

