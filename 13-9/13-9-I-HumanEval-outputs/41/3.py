
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    return sorted([element for element in x if all(digit % 2 != 0 for digit in str(element))])

