
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    l_prime = l.copy()
    for i in range(len(l_prime)):
        if i % 3 == 0:
            l_prime[i] = sorted(l_prime[i:i+3])[0]
    return l_prime

