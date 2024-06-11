from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_value = 0
    result = []
    for number in numbers:
        if number > max_value:
            max_value = number
        result.append(max_value)
    return result


