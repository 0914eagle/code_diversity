
from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    
    if a < 0 or b < 0:
        raise ValueError("a and b must be positive integers")

    if a > b:
        a, b = b, a

    return [i for i in range(a, b+1) if i % 2 == 0]

