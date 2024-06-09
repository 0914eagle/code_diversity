
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    result = []
    for idx, num in enumerate(l):
        if idx % 3 == 0:
            result.append(num)
    sorted_thirds = sorted(result)
    return [sorted_thirds.pop(0) if i % 3 == 0 else num for i, num in enumerate(l)]

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
