from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_number = numbers[0]
    result = [max_number]
    for number in numbers[1:]:
        max_number = max(max_number, number)
        result.append(max_number)
    return result


