
from typing import List

def monotonic(l: List[int]) -> bool:
    
    if len(l) <= 1:
        return True
    else:
        return all(l[i] <= l[i+1] or l[i] >= l[i+1] for i in range(len(l)-1))

