
from typing import List

def sort_third(l: List[int]) -> List[int]:
    sorted_indices = sorted([i for i in range(len(l)) if i % 3 == 0], key=lambda x: l[x])
    sorted_values = [l[i] for i in sorted_indices]
    
    result = l.copy()
    for i, val in zip(sorted_indices, sorted_values):
        result[i] = val
    
    return result

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
