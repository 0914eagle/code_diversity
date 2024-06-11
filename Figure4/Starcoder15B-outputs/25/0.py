from typing import List


def factorize(n: int) -> List[int]:
    
    factors = []
    i = 2
    while n != 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i += 1
    return factors


if __name__ == '__main__':
    print(factorize(int(input())))
/README.md
# Python-Course

## Description

