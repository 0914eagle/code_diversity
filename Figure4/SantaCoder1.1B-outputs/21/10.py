from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("rescale_to_unit requires at least two numbers")
    min_val = min(numbers)
    max_val = max(numbers)
    return [float(x - min_val) / (max_val - min_val) for x in numbers]


