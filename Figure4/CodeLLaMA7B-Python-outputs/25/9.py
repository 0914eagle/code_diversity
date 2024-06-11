from typing import List


def factorize(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("Input number should be positive")
    if n == 1:
        return []
    result = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            result.append(i)
            n //= i
        i += 1
    if n > 1:
        result.append(n)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
