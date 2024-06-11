from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    if not numbers:
        return []
    max_number = numbers[0]
    result = [max_number]
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
        result.append(max_number)
    return result


