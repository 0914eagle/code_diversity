from typing import List


def factorize(n: int) -> List[int]:
    
    if n < 2:
        return []
    factors = []
    while n > 1:
        if n % 2 == 0:
            n //= 2
            factors.append(2)
        else:
            n = n - 1
            factors.append(1)
    return factors


