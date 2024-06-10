
from typing import List

def can_arrange(arr: List[int]) -> int:
    def find_largest_index(arr: List[int]) -> int:
        max_index = -1
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] <= arr[i - 1]:
                max_index = i
                break
        return max_index

    if not arr or len(arr) == 1:
        print(-1)
        return

    result = find_largest_index(arr)
    print(result)

# Test cases
can_arrange([1, 2, 4, 3, 5])
can_arrange([1, 2, 3])
