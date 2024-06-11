from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_so_far = []
    for i in range(len(numbers)):
        if i == 0:
            max_so_far.append(numbers[0])
        else:
            max_so_far.append(max(numbers[i], max_so_far[-1]))
    return max_so_far


