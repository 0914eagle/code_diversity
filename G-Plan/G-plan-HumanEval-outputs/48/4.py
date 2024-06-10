
from typing import List

def smallest_change(arr: List[int]) -> int:
    def is_palindromic(arr):
        return arr == arr[::-1]

    changes = 0
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            changes += 1
        left += 1
        right -= 1

    return changes

# Test cases
arr1 = [1, 2, 3, 5, 4, 7, 9, 6]
arr2 = [1, 2, 3, 4, 3, 2, 2]
arr3 = [1, 2, 3, 2, 1]

print(smallest_change(arr1))
print(smallest_change(arr2))
print(smallest_change(arr3))
