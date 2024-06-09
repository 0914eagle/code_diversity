
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    
    # sort the list
    l.sort()
    # loop through the list and find three distinct elements that sum to zero
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

