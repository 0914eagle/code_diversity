
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    
    result = []
    max_val = None
    for num in numbers:
        if max_val is None or num > max_val:
            max_val = num
        result.append(max_val)
    return result

