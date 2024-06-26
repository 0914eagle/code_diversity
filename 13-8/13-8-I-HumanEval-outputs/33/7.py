
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value

    return [(number - min_value) / range_value for number in numbers]

