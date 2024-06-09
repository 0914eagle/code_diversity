
from typing import List

def double_the_difference(lst: List[float]) -> int:
    
    sum_of_squares = 0
    for num in lst:
        if num < 0 or not num.is_integer():
            continue
        if num % 2 == 1:
            sum_of_squares += num ** 2
    return sum_of_squares

