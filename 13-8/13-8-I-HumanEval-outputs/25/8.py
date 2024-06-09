
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    
    rolling_max_list = []
    max_value = -float('inf')
    for num in numbers:
        max_value = max(max_value, num)
        rolling_max_list.append(max_value)
    return rolling_max_list

