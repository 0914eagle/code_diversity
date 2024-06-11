from typing import List


def factorize(n: int) -> List[int]:
    
    if n < 1:
        raise ValueError("Input number should be greater than 0")
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
