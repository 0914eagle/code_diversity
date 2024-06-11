from typing import List


def factorize(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("Only positive numbers are allowed")

    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            result.append(i)
            n //= i

    if n > 2:
        result.append(n)

    return result


if