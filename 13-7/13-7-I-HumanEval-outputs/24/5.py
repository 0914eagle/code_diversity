
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    # Your code here
    return sorted([num for num in x if all(int(digit) % 2 != 0 for digit in str(num))])

