
from typing import List

def add(lst: List[int]) -> int:
    
    result = 0
    for i, num in enumerate(lst):
        if num % 2 == 0 and i % 2 == 1:
            result += num
    return result

