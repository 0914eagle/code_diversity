
from typing import List

def sort_third(l: List[int]) -> List[int]:
    new_list = l.copy()
    divisible_by_three = [val for idx, val in enumerate(l) if idx % 3 == 0]
    divisible_by_three.sort()
    
    for idx, val in enumerate(new_list):
        if idx % 3 == 0:
            new_list[idx] = divisible_by_three.pop(0)
    
    return new_list

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
