
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(x - mean) for x in numbers]

    # Calculate the average of the absolute differences
    return sum(absolute_deviations) / len(numbers)

