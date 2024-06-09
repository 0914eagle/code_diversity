
from typing import List
import math

def sum_squares(lst: List[float]) -> int:
    total = 0
    for num in lst:
        rounded_num = math.ceil(num)
        total += rounded_num ** 2
    return total

# Test cases
print(sum_squares([1.0, 2.0, 3.0]))  # Output: 14
print(sum_squares([1.0, 4.0, 9.0]))  # Output: 98
print(sum_squares([1.0, 3.0, 5.0, 7.0]))  # Output: 84
print(sum_squares([1.4, 4.2, 0.0]))  # Output: 29
print(sum_squares([-2.4, 1.0, 1.0]))  # Output: 6
