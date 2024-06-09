
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    
    result = []
    for i in range(len(numbers)):
        max_value = max(numbers[:i+1])
        result.append(max_value)
    return result

