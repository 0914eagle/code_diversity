
from typing import List

def add(lst: List[int]) -> int:
    
    result = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            result += lst[i]
    return result

