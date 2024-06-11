from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    assert len(numbers) >= 2
    min_number = min(numbers)
    max_number = max(numbers)
    return [x / (max_number - min_number) for x in numbers]


