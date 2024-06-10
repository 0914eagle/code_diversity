
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    l_prime = []
    for i, x in enumerate(l):
        if i % 3 == 0:
            l_prime.append(x)
        else:
            l_prime.extend(sorted([x]))
    return l_prime

