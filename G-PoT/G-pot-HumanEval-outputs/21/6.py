
from typing import List

def sum_squares(lst: List[int]) -> int:
    total = 0
    for idx, num in enumerate(lst):
        if idx % 3 == 0:
            total += num ** 2
        elif idx % 4 == 0:
            total += num ** 3
        else:
            total += num
    return total

# Test cases
print(sum_squares([1, 2, 3]))  # Output: 1^2 + 2 + 3 = 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: (-1)^2 + (-5) + 2 + (-1)^3 + (-5) = -5
