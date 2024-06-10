
from typing import List

def is_sorted(lst: List[int]) -> bool:
    def has_more_than_one_duplicate(lst: List[int]) -> bool:
        counts = {}
        for num in lst:
            if num in counts:
                counts[num] += 1
                if counts[num] > 1:
                    return True
            else:
                counts[num] = 1
        return False

    def is_sorted_ascending(lst: List[int]) -> bool:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True

    if has_more_than_one_duplicate(lst):
        return False

    if is_sorted_ascending(lst):
        return True
    else:
        return False

# Read input list
input_list = list(map(int, input().strip().split(',')))

# Call the function and print the result
print(is_sorted(input_list))
