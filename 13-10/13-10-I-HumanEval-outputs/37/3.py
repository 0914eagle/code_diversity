
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                if l[i] + l[j] + l[k] == 0 and i != j and j != k and i != k:
                    return True
    return False

