
from typing import List

def add(lst: List[int]) -> int:
    
    if len(lst) == 0:
        return 0
    sum = 0
    for i in range(1, len(lst), 2):
        sum += lst[i]
    return sum

