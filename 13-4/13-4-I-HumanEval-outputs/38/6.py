
from typing import List

def double_the_difference(lst: List[float]) -> int:
    
    result = 0
    for num in lst:
        if num < 0 or not num.is_integer():
            continue
        if num % 2 == 1:
            result += num ** 2
    return result

