
from typing import List

def add(lst: List[int]) -> int:
    
    result = 0
    for i, num in enumerate(lst):
        if i % 2 == 1 and num % 2 == 0:
            result += num
    return result

