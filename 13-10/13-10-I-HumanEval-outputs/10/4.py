
from typing import List

def monotonic(l: List[int]) -> bool:
    
    if len(l) <= 1:
        return True
    elif l[0] > l[1]:
        for i in range(1, len(l)):
            if l[i] >= l[i-1]:
                return False
    else:
        for i in range(1, len(l)):
            if l[i] <= l[i-1]:
                return False
    return True

