
from typing import List

def factorize(n: int) -> List[int]:
    
    factors = []
    while n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                n = n // i
                break
        else:
            factors.append(n)
            n = 1
    return factors

