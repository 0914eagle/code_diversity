from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("Cannot rescale to unit with less than two elements")
    min_value = min(numbers)
    max_value = max(numbers)
    return [x / (max_value - min_value) for x in numbers]


