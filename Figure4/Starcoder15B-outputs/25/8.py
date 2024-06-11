from typing import List


def factorize(n: int) -> List[int]:
    
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
    return factors


if __name__ == '__main__':
    import doctest
    doctest.testmod()