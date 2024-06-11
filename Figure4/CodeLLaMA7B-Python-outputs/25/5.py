from typing import List


def factorize(n: int) -> List[int]:
    
    if n < 1:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return [1]
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


if