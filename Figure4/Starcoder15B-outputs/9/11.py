from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    result = []
    for i in range(len(numbers)):
        result.append(max(numbers[0:i + 1]))
    return result


