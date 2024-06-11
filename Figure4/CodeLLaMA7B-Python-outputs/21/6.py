from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    min_value = min(numbers)
    max_value = max(numbers)
    if min_value == max_value:
        return [0.0] * len(numbers)
    return [(x - min_value) / (max_value - min_value) for x in numbers]


if