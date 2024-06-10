
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    
    # sort the list
    l.sort()
    # iterate over the list
    for i in range(len(l) - 2):
        # check if the current element is zero
        if l[i] == 0:
            # if it is, return True
            return True
        # calculate the sum of the current element with the next two elements
        sum1 = l[i] + l[i + 1]
        sum2 = l[i] + l[i + 2]
        # check if the sum is zero
        if sum1 == 0 or sum2 == 0:
            # if it is, return True
            return True
    # if we reach this point, no triplet was found
    return False

