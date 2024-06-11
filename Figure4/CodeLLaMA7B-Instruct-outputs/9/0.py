
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    result: List[int] = []
    max_value: int = 0
    for num in numbers:
        max_value = max(max_value, num)
        result.append(max_value)
    return result

