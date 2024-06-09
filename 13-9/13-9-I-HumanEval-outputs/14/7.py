
from typing import List

def sum_squares(lst: List[float]) -> int:
    
    return sum(int(ceil(x) ** 2 for x in lst))

