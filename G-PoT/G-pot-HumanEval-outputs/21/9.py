
from typing import List

def sum_squares(lst: List[int]) -> int:
    total = 0
    for idx, num in enumerate(lst):
        if idx % 3 == 0:
            total += num ** 2
        elif idx % 4 == 0 and idx % 3 != 0:
            total += num ** 3
        else:
            total += num
    return total
