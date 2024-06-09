
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    # Your code here
    l_even = l[::2]
    l_even.sort()
    l_odd = l[1::2]
    return l_odd + l_even

