
from typing import List

def is_sorted(arr: List[int]) -> bool:
    return arr == sorted(arr)

def max_at_last(arr: List[int]) -> bool:
    return arr.index(max(arr)) == len(arr) - 1

def is_cyclic_shift(arr: List[int]) -> bool:
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        if arr == sorted_arr:
            return True
        arr = arr[-1:] + arr[:-1]
    return False

def count_inversions(arr: List[int]) -> bool:
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions % 2 == 0

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(',')))
    print(is_sorted(arr) or max_at_last(arr) or is_cyclic_shift(arr) or count_inversions(arr))
