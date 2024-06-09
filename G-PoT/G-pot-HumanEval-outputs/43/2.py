
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    result = []
    sorted_values = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    sorted_index = 0
    for i in range(len(l)):
        if i % 3 == 0:
            result.append(sorted_values[sorted_index])
            sorted_index += 1
        else:
            result.append(l[i])
    return result
