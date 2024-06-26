
from typing import List

def sum_squares(lst: List[int]) -> int:
    
    result = 0
    for i, x in enumerate(lst):
        if i % 3 == 0:
            result += x**2
        elif i % 4 == 0 and i % 3 != 0:
            result += x**3
        else:
            result += x
    return result

