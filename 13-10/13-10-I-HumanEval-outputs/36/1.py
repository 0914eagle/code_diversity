
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    result = []
    for num in x:
        if all(digit % 2 != 0 for digit in str(num)):
            result.append(num)
    return sorted(result)

