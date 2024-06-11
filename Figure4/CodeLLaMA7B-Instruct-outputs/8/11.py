
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    sum_val = 0
    prod_val = 1
    for num in numbers:
        sum_val += num
        prod_val *= num
    return sum_val, prod_val

