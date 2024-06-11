from typing import List


def factorize(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("n must be a positive number")

    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            result.append(i)
            n //= i
        i += 2

    if n > 2:
        result.append(n)

    return result


if