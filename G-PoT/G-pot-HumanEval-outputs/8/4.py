
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    
    if not numbers:
        return []

    max_list = [numbers[0]]
    for i in range(1, len(numbers)):
        max_list.append(max(numbers[i], max_list[i - 1]))

    return max_list
