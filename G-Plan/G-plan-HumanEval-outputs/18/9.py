
from typing import List

def is_sorted(lst: List[int]) -> bool:
    def has_more_than_one_duplicate(lst: List[int]) -> bool:
        counts = {}
        for num in lst:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > 1:
                return True
        return False

    def is_sorted_ascending(lst: List[int]) -> bool:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True

    if has_more_than_one_duplicate(lst):
        return False

    return is_sorted_ascending(lst)

# Read input list
lst = list(map(int, input().strip()[1:-1].split(',')))

# Output the result
print(is_sorted(lst))
