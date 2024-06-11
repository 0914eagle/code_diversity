from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    return sum(abs(x - mean(numbers)) for x in numbers) / len(numbers)


