
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(map(lambda x: abs(x - mean), numbers)) / len(numbers)

