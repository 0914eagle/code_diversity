from typing import List


def factorize(n: int) -> List[int]:
    
    if n == 1:
        return []
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors


if __name__ == '__main__':
    print(factorize(