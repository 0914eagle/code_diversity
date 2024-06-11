from typing import List


def factorize(n: int) -> List[int]:
    
    factors = []
    i = 2
    while i ** 2 <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
