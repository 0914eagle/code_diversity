
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    l_prime = l.copy()
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime[i] = sorted(l[i:i+3])[0]
    return l_prime

