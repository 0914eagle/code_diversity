
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    
    # Initialize a set to store the unique elements in the list
    unique_elements = set()
    # Iterate over the list and check if there are three distinct elements that sum to zero
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0 and l[i] != l[j] != l[k] != 0:
                    return True
    return False


