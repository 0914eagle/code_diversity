from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    if not numbers:
        return []
    max_list = []
    for i in range(len(numbers)):
        max_list.append(max(numbers[i - 1:i + 1]))
    return max_list


