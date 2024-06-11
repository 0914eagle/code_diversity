from typing import List


def factorize(n: int) -> List[int]:
    
    if n == 1:
        return []
    if n < 1:
        raise ValueError
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i += 1
    return factors


if