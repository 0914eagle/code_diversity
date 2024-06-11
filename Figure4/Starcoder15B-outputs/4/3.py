from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)
/tests/test_mean_absolute_deviation.py
from statistics import mean
from typing import List

from src.mean_absolute_deviation import mean_absolute_deviation


