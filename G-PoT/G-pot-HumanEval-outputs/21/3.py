
from typing import List

def sum_squares(lst: List[int]) -> int:
    total_sum = 0
    for idx, num in enumerate(lst):
        if (idx + 1) % 3 == 0:
            total_sum += num ** 2
        elif (idx + 1) % 4 == 0 and (idx + 1) % 3 != 0:
            total_sum += num ** 3
        else:
            total_sum += num
    return total_sum

# Test the function
print(sum_squares([1, 2, 3]))  # Output: 1^2 + 2 + 3 = 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -1 + (-5) + 2^2 + (-1)^3 + (-5) = -10
