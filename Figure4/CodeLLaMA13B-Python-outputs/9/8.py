from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_so_far = -1
    result = []
    for number in numbers:
        max_so_far = max(max_so_far, number)
        result.append(max_so_far)
    return result


