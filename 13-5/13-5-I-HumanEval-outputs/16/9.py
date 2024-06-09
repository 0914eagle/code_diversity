
from typing import List

def tri(n: int) -> List[int]:
    
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n == 0:
        return [1]
    
    tribonacci_seq = [0, 1, 3]
    for i in range(n-2):
        tribonacci_seq.append(tribonacci_seq[-1] + tribonacci_seq[-2] + tribonacci_seq[-3])
    
    return tribonacci_seq

