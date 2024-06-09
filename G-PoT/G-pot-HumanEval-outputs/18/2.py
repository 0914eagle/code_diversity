
from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    
    common_elements = list(set(l1) & set(l2))
    return sorted(common_elements)
