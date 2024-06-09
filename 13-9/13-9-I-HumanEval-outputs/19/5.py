
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    return [x for i, x in enumerate(l) if i % 2 == 0] + sorted([x for i, x in enumerate(l) if i % 2 == 1])

