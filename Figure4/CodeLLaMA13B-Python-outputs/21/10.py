from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_num = min(numbers)
    max_num = max(numbers)
    return [round((num - min_num) / (max_num - min_num), 2) for num in numbers]


if