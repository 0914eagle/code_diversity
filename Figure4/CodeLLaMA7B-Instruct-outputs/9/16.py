
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    if not numbers:
        return []

    rolling_max_list: List[int] = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > rolling_max_list[-1]:
            rolling_max_list.append(numbers[i])
        else:
            rolling_max_list.append(rolling_max_list[-1])

    return rolling_max_list

