
from typing import List

def factorize(n: int) -> List[int]:
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

    factors = trial_division(n)
    print(factors)

factorize(int(input()))
