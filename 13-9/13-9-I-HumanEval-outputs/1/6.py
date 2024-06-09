
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    
    result = []
    rolling_max_val = None
    for num in numbers:
        if rolling_max_val is None or num > rolling_max_val:
            rolling_max_val = num
        result.append(rolling_max_val)
    return result

