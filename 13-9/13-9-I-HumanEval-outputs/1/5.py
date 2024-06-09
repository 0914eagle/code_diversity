
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    
    rolling_max_list = []
    for i in range(len(numbers)):
        rolling_max_list.append(max(numbers[:i+1]))
    return rolling_max_list

