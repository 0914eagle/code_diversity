from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_so_far = -1
    max_list = []
    for i in numbers:
        if i > max_so_far:
            max_so_far = i
        max_list.append(max_so_far)
    return max_list


