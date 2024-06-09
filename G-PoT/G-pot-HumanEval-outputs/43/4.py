
from typing import List

def sort_third(l: List[int]) -> List[int]:
    result = []
    for i, num in enumerate(l):
        if i % 3 == 0:
            result.append(num)
    sorted_thirds = sorted(result)
    index = 0
    for i, num in enumerate(l):
        if i % 3 == 0:
            result[i] = sorted_thirds[index]
            index += 1
        else:
            result[i] = num
    return result

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
