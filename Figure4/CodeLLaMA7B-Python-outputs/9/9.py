from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_so_far = [numbers[0]]
    for i in range(1, len(numbers)):
        max_so_far.append(max(numbers[i], max_so_far[-1]))
    return max_so_far


