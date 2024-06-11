from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_num = -1
    max_num_list = []
    for num in numbers:
        max_num = max(max_num, num)
        max_num_list.append(max_num)
    return max_num_list


