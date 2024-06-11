from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_value = numbers[0]
    max_values = [max_value]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
        max_values.append(max_value)
    return max_values


