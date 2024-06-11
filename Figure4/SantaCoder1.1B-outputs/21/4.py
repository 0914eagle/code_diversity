from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("Cannot rescale list of length < 2")
    min_num = min(numbers)
    max_num = max(numbers)
    return [num - min_num for num in numbers]

