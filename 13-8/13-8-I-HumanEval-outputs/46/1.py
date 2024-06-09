
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    return [l[i] for i in range(len(l)) if i % 2 == 0] + sorted([l[i] for i in range(len(l)) if i % 2 == 1])

