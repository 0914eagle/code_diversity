
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    return sorted([num for num in x if all(digit not in [0, 2, 4, 6, 8] for digit in str(num))])

