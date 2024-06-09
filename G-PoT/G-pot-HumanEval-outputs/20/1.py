
from typing import List

def sort_even(l: List[int]) -> List[int]:
    even_values = sorted([x for x in l[::2]])
    result = []
    for i, val in enumerate(l):
        if i % 2 == 0:
            result.append(even_values.pop(0))
        else:
            result.append(val)
    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
