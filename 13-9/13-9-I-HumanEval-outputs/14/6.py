
from typing import List

def sum_squares(lst: List[float]) -> int:
    
    return sum(int(round(i**2)) for i in lst)

