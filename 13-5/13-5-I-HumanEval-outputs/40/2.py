
from typing import List

def add(lst: List[int]) -> int:
    
    result = 0
    for i, elem in enumerate(lst):
        if elem % 2 == 0 and i % 2 == 1:
            result += elem
    return result

