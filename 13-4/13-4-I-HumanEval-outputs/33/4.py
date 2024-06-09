
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    l_prime = l.copy()
    for i in range(len(l)):
        if i % 3 == 0:
            continue
        l_prime[i] = l[i]
    for i in range(0, len(l), 3):
        l_prime[i:i+3] = sorted(l_prime[i:i+3])
    return l_prime

