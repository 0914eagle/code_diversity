
from typing import List

def f(n: int) -> List[int]:
    
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i + 1)))
    return result

def factorial(n: int) -> int:
    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

