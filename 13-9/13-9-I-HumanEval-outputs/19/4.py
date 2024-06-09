
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    l_odd = [x for i, x in enumerate(l) if i % 2 == 0]
    l_even = [x for i, x in enumerate(l) if i % 2 == 1]
    return l_odd + sorted(l_even)

