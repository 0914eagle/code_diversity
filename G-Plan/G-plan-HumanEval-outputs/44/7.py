
from typing import List

def trial_division(n: int) -> List[int]:
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors

def factorize(n: int) -> List[int]:
    return trial_division(n)

n = int(input())
result = factorize(n)
print(result)
