
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    
    # sort the list
    l.sort()
    # iterate over the list
    for i in range(len(l) - 2):
        # find the two numbers that sum to -l[i]
        lo = i + 1
        hi = len(l) - 1
        while lo < hi:
            if l[lo] + l[hi] == -l[i]:
                return True
            elif l[lo] + l[hi] > -l[i]:
                hi -= 1
            else:
                lo += 1
    return False

