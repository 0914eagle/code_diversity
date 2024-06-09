
from typing import List

def add(lst: List[int]) -> int:
    
    result = 0
    for i, x in enumerate(lst):
        if x % 2 == 0 and i % 2 == 1:
            result += x
    return result

