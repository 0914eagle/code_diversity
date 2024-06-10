
from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    
    if len(lst) < 2:
        return None
    sorted_list = sorted(lst)
    return sorted_list[1]

