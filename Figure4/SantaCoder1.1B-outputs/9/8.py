from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    if not numbers:
        return []
    result = []
    for i in range(len(numbers)):
        result.append(max(numbers[i - 1:i + 1]))
    return result


