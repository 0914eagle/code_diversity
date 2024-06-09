
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    
    # sort the list
    l.sort()
    # loop through the list
    for i in range(len(l) - 2):
        # check if the sum of the first two elements is zero
        if l[i] == 0:
            return True
        # check if the sum of the first two elements is negative
        if l[i] < 0:
            # check if the sum of the last two elements is positive
            if l[i + 1] + l[i + 2] > 0:
                return False
            # check if the sum of the last two elements is zero
            if l[i + 1] + l[i + 2] == 0:
                return True
        # check if the sum of the first two elements is positive
        if l[i] > 0:
            # check if the sum of the last two elements is negative
            if l[i + 1] + l[i + 2] < 0:
                return False
    return False

