
from typing import List

def is_sorted(lst: List[int]) -> bool:
    def has_duplicates(lst: List[int]) -> bool:
        seen = set()
        for num in lst:
            if num in seen:
                return True
            seen.add(num)
        return False

    def is_sorted_ascending(lst: List[int]) -> bool:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True

    if has_duplicates(lst):
        return False

    return is_sorted_ascending(lst)

# Test the function with provided examples
print(is_sorted([5]))  # True
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # False
