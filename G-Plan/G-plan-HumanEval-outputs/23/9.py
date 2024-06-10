
from typing import List

def can_arrange(arr: List[int]) -> int:
    def find_largest_index(arr: List[int]) -> int:
        max_index = -1
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] <= arr[i - 1]:
                max_index = i
                break
        return max_index

    return find_largest_index(arr)

# Test cases
if __name__ == "__main__":
    arr1 = [1, 2, 4, 3, 5]
    arr2 = [1, 2, 3]
    print(can_arrange(arr1))  # Output: 3
    print(can_arrange(arr2))  # Output: -1
