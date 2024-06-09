
from typing import List

def by_length(arr: List[int]) -> List[str]:
    
    if not arr:
        return []
    
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = []
    for num in arr:
        if 1 <= num <= 9:
            result.append(names[num - 1])
    
    result.reverse()
    return result

