
from typing import List

def derivative(xs: List[int]) -> List[int]:
    
    return [i * x for i, x in enumerate(xs[1:], 1)]

