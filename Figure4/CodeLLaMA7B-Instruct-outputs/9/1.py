
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    result: List[int] = []
    current_max: int = 0

    for num in numbers:
        current_max = max(current_max, num)
        result.append(current_max)

    return result

