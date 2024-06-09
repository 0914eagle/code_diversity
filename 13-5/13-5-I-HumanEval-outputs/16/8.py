
from typing import List

def tri(n: int) -> List[int]:
    
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    tribonacci_seq = [0, 0, 1, 3]
    for i in range(n):
        if i % 2 == 0:
            tribonacci_seq.append(1 + i / 2)
        else:
            tribonacci_seq.append(tribonacci_seq[i - 1] + tribonacci_seq[i - 2] + tribonacci_seq[i + 1])
    
    return tribonacci_seq[:n + 1]

