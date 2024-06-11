
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    smallest = min(numbers)
    largest = max(numbers)
    range_ = largest - smallest
    return [((x - smallest) / range_) for x in numbers]

