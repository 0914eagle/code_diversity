
from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    
    # Check if the list is balanced
    if q == q[::-1]:
        # Check if the sum of the elements is less than or equal to the maximum possible weight
        if sum(q) <= w:
            return True
    return False

