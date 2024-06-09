
from typing import List

def monotonic(l: List[int]) -> bool:
    
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

