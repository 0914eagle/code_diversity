
from typing import List

def tri(n: int) -> List[int]:
    
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    else:
        tribonacci_seq = [1, 3]
        for i in range(2, n+1):
            if i % 2 == 0:
                tribonacci_seq.append(1 + i // 2)
            else:
                tribonacci_seq.append(tribonacci_seq[i-1] + tribonacci_seq[i-2] + tribonacci_seq[i+1])
        return tribonacci_seq

