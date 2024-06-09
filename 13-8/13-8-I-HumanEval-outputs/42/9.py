
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    
    x_mean = sum(numbers) / len(numbers)
    deviation = [abs(x - x_mean) for x in numbers]
    return sum(deviation) / len(deviation)

