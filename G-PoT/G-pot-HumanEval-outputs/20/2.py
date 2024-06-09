
from typing import List

def sort_even(l: List[int]) -> List[int]:
    even_indices = sorted([num for idx, num in enumerate(l) if idx % 2 == 0])
    result = [num if idx % 2 != 0 else even_indices.pop(0) for idx, num in enumerate(l)]
    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
