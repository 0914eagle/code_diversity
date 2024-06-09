
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    
    numbers = [float(number) for number in numbers]
    mean = sum(numbers) / len(numbers)
    deviations = [abs(number - mean) for number in numbers]
    return sum(deviations) / len(numbers)

