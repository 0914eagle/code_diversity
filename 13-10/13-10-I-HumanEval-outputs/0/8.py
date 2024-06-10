
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    # Your code here
    l_prime = [None] * len(l)
    for i, v in enumerate(l):
        if i % 3 == 0:
            l_prime[i] = sorted([l[i + j] for j in range(3) if i + j < len(l)])
        else:
            l_prime[i] = v
    return l_prime

