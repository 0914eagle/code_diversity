from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_so_far = [numbers[0]]
    for i in range(1, len(numbers)):
        max_so_far.append(max(max_so_far[i - 1], numbers[i]))
    return max_so_far


