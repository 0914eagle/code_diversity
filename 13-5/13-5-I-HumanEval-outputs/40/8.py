
from typing import List

def add(lst: List[int]) -> int:
    
    result = 0
    for i, x in enumerate(lst):
        if i % 2 == 0 and x % 2 == 0:
            result += x
    return result

