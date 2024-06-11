from typing import List


def factorize(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("Input value should be positive")
    result = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                result.append(i)
                n = n // i
                break
    return result


if __name__ ==