
from typing import List

def monotonic(l: List[int]) -> bool:
    
    if len(l) < 2:
        return True
    diff = l[1] - l[0]
    for i in range(2, len(l)):
        if (l[i] - l[i-1]) * diff < 0:
            return False
    return True

