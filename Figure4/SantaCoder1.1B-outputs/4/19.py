from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    return sum(abs(x - numbers[len(numbers) // 2]) for x in numbers) / len(numbers)


if