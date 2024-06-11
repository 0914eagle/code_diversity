from typing import List


def factorize(n: int) -> List[int]:
    
    factors = []
    while n > 1:
        if n % 2 == 0:
            n //= 2
            continue
        if n % 3 == 0:
            n //= 3
            continue
        if n % 5 == 0:
            n //= 5
            continue
        factors.append(n)
        n = n - 1
    return factors


