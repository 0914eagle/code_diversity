
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    l_even = [l[i] for i in range(len(l)) if i % 2 == 0]
    l_even.sort()
    l_even = [l[i] for i in range(len(l)) if i % 2 == 1]
    return l_even

