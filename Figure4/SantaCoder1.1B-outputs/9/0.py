from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(numbers[i])
        else:
            result.append(max(numbers[i - 1], numbers[i]))
    return result


