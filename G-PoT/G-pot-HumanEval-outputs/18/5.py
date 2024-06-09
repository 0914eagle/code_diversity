
from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    
    common_elements = list(set(l1) & set(l2))
    return sorted(common_elements)

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]
