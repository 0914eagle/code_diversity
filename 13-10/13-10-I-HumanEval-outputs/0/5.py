
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    l_sorted = sorted(l)
    l_prime = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime.append(l_sorted[i])
        else:
            l_prime.append(l[i])
    return l_prime

