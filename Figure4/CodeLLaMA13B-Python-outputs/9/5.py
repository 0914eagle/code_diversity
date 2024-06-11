from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    rolling_max_list = []
    max_number = numbers[0]
    for number in numbers:
        max_number = max(max_number, number)
        rolling_max_list.append(max_number)
    return rolling_max_list


