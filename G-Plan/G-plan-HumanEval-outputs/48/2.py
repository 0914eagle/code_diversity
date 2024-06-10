
from typing import List

def smallest_change(arr: List[int]) -> int:
    def is_palindromic(array):
        return array == array[::-1]

    changes = 0
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            changes += 1
        left += 1
        right -= 1

    return changes

# Test the function
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    result = smallest_change(arr)
    print(result)
