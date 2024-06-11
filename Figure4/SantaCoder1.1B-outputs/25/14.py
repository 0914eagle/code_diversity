from typing import List


def factorize(n: int) -> List[int]:
    
    factors = []
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            factors.append(2)
            n -= 1
    if n > 1:
        factors.append(n)
    return factors


