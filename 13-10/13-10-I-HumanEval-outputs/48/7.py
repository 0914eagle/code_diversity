
from typing import List

def median(l: List[int]) -> float:
    
    l.sort()
    length = len(l)
    if length % 2 == 0:
        return (l[length // 2 - 1] + l[length // 2]) / 2
    else:
        return l[length // 2]

