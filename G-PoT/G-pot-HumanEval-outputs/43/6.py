
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    sorted_indices = sorted([i for i in range(len(l)) if i % 3 == 0], key=lambda x: l[x])
    result = l.copy()
    for i in sorted_indices:
        result[i] = l[i]
    return result
