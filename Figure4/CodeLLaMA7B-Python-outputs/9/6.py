from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_so_far = [numbers[0]]
    for number in numbers[1:]:
        max_so_far.append(max(number, max_so_far[-1]))
    return max_so_far


