
from typing import List

def tri(n: int) -> List[int]:
    
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return [1]
    if n == 1:
        return [1, 3]
    result = [1, 3]
    for i in range(2, n):
        if i % 2 == 0:
            result.append(1 + i // 2)
        else:
            result.append(result[i - 1] + result[i - 2] + result[i + 1])
    return result

