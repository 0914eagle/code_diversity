
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    unique_digits = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            unique_digits.append(num)
    return sorted(unique_digits)

