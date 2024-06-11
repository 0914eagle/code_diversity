from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_number = min(numbers)
    max_number = max(numbers)
    return [round((number - min_number) / (max_number - min_number), 2) for number in numbers]


if