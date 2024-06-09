
from typing import List

def double_the_difference(lst: List[float]) -> int:
    
    result = 0
    for num in lst:
        if num > 0 and num % 2 != 0:
            result += num ** 2
    return result

