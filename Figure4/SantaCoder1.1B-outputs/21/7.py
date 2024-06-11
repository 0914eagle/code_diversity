from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    assert len(numbers) >= 2
    min_val = min(numbers)
    max_val = max(numbers)
    return [x / (max_val - min_val) for x in numbers]


