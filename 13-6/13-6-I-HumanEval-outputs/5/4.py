
from typing import List

def factorize(n: int) -> List[int]:
    
    if n == 1:
        return [1]
    
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.extend([i, i])
            n //= i
        while n % i == 0:
            n //= i
    
    if n > 1:
        factors.append(n)
    
    return factors

