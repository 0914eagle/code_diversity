
from typing import List

def monotonic(l: List[int]) -> bool:
    
    if len(l) <= 1:
        return True
    else:
        return all(l[i+1] >= l[i] for i in range(len(l)-1)) or all(l[i+1] <= l[i] for i in range(len(l)-1))

