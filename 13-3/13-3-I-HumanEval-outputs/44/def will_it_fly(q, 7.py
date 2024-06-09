
from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    
    # check if the list is palindromic
    if q == q[::-1]:
        # check if the sum of the elements is less than or equal to the maximum possible weight
        if sum(q) <= w:
            return True
    return False

