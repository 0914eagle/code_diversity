from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_value = numbers[0]
    result = [max_value]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
        result.append(max_value)
    return result

