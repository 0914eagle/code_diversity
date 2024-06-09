
from typing import List

def sum_squares(lst: List[int]) -> int:
    total_sum = 0
    for idx, num in enumerate(lst):
        if idx % 3 == 0:
            total_sum += num ** 2
        elif idx % 4 == 0:
            total_sum += num ** 3
        else:
            total_sum += num
    return total_sum
