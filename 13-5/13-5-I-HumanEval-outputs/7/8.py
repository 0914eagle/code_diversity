
from typing import List

def derivative(xs: List[int]) -> List[int]:
    
    derivative_coeffs = []
    for i in range(1, len(xs)):
        derivative_coeffs.append(i * xs[i])
    return derivative_coeffs

