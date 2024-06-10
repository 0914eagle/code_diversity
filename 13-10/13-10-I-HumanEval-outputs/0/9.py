
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    l_prime = []
    for i, elem in enumerate(l):
        if i % 3 == 0:
            l_prime.append(elem)
        else:
            l_prime.append(sorted(l[i-1:i+2])[1])
    return l_prime

