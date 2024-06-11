from typing import List


def factorize(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("Input number should be greater than 0")
    if n == 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


if