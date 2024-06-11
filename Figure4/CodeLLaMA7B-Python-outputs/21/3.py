from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("At least two elements are required")
    min_value = min(numbers)
    max_value = max(numbers)
    if min_value == max_value:
        raise ValueError("All numbers are the same")
    return [(x - min_value) / (max_value - min_value) for x in numbers]


if __name__ ==