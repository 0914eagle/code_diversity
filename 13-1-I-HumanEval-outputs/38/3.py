
from typing import List

def by_length(arr: List[int]) -> List[str]:
    
    # Your code here
    if not arr:
        return []
    
    sorted_arr = sorted(arr, key=lambda x: x if x in range(1, 10) else float('inf'))
    reversed_arr = sorted_arr[::-1]
    result = []
    for num in reversed_arr:
        if num in range(1, 10):
            result.append(f'{num}')
    
    return result

