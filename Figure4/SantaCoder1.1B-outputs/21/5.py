from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("rescale_to_unit requires at least two numbers")
    min_num = min(numbers)
    max_num = max(numbers)
    return [num - min_num for num in numbers]


