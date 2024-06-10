
from typing import List

def is_palindromic(arr: List[int]) -> bool:
    return arr == arr[::-1]

def smallest_change(arr: List[int]) -> int:
    changes = 0
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            changes += 1
        left += 1
        right -= 1

    return changes

# Test the function with the provided examples
print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
