from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    rolling_max_list: List[int] = []
    max_number: int = numbers[0]
    for number in numbers:
        rolling_max_list.append(max_number)
        if number > max_number:
            max_number = number
    return rolling_max_list


