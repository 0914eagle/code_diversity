
from typing import List

def can_arrange(arr: List[int]) -> int:
    def find_largest_index(arr):
        max_index = -1
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] <= arr[i - 1]:
                max_index = i
                break
        return max_index

    arr = list(map(int, arr.strip('[]').split(', ')))
    result = find_largest_index(arr)
    print(result)

can_arrange(input())
