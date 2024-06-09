
from typing import List, Union
import math

def sum_squares(lst: List[float]) -> int:
    total = 0
    for num in lst:
        rounded_num = math.ceil(num)
        total += rounded_num ** 2
    return total
