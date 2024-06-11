from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    if not numbers:
        return []
    rolling_max_list = [numbers[0]]
    for number in numbers[1:]:
        rolling_max_list.append(max(rolling_max_list[-1], number))
    return rolling_max_list


