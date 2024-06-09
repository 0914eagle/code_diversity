
from typing import List

def tri(n: int) -> List[int]:
    
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    result = [0] * (n + 1)
    result[0] = 1
    result[1] = 3
    
    for i in range(2, n + 1):
        if i % 2 == 0:
            result[i] = result[i - 1] + result[i - 2] + result[i - 1]
        else:
            result[i] = 1 + result[i - 1] / 2
    
    return result

