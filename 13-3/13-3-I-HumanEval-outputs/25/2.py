
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    
    # sort the list
    l.sort()
    # loop through the list
    for i in range(len(l) - 2):
        # find the sum of the first two elements
        sum1 = l[i] + l[i + 1]
        # find the sum of the last two elements
        sum2 = l[len(l) - 1] + l[len(l) - 2]
        # check if the sum is zero
        if sum1 == 0 or sum2 == 0:
            return True
    return False

