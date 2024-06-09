
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    
    # sort the list
    l.sort()
    # iterate over the list
    for i in range(len(l) - 2):
        # find the sum of the first two elements
        a = l[i]
        b = l[i + 1]
        c = -a - b
        # check if the sum is zero
        if c in l[i + 2:]:
            # return True if the sum is zero and the elements are distinct
            return True
    # return False if no triplet sum to zero
    return False

