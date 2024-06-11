from typing import List


def factorize(n: int) -> List[int]:
    
    if n == 1:
        return []
    for i in range(2, n + 1):
        if n % i == 0:
            return [i] + factorize(n // i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()