
from typing import List

def sort_even(l: List[int]) -> List[int]:
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    sorted_even_values = sorted([l[i] for i in even_indices])
    
    result = l.copy()
    for i, val in zip(even_indices, sorted_even_values):
        result[i] = val
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
