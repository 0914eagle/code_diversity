
from typing import List

def sum_squares(lst: List[float]) -> int:
    
    # Your code here
    return sum(int(math.ceil(x)) ** 2 for x in lst)

