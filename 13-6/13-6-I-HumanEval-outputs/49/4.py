
from typing import List

def f(n: int) -> List[int]:
    
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(math.factorial(i))
        else:
            result.append(sum(range(1, i + 1)))
    return result

