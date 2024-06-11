from typing import List


def factorize(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return [1]
    factors = []
    i = 2
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


if