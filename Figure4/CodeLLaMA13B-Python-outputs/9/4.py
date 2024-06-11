from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_value = -1
    max_list = []
    for number in numbers:
        if number > max_value:
            max_value = number
        max_list.append(max_value)
    return max_list


