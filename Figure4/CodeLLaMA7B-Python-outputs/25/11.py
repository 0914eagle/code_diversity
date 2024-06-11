from typing import List


def factorize(n: int) -> List[int]:
    
    result = []
    i = 2
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            result.append(i)
    if n > 1:
        result.append(n)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
