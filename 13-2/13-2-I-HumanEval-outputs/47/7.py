
from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    
    if len(lst) < 2:
        return None
    sorted_lst = sorted(lst)
    return sorted_lst[1]

