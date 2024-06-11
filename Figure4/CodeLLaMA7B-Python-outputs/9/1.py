from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    rolling_max_list = []
    rolling_max_value = numbers[0]
    for number in numbers:
        if number > rolling_max_value:
            rolling_max_value = number
        rolling_max_list.append(rolling_max_value)
    return rolling_max_list


