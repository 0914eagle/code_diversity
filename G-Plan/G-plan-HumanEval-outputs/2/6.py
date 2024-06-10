
from typing import List

def is_sorted(arr: List[int]) -> bool:
    return arr == sorted(arr)

def max_at_last(arr: List[int]) -> bool:
    return arr.index(max(arr)) == len(arr) - 1

def is_cyclic_shift(sorted_arr: List[int], arr: List[int]) -> bool:
    n = len(arr)
    for i in range(n):
        if arr == sorted_arr:
            return True
        arr = [arr[-1]] + arr[:-1]
    return False

def count_inversions(arr: List[int]) -> bool:
    inversions = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions % 2 == 0

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    sorted_arr = sorted(arr)
    
    if is_sorted(arr) or max_at_last(arr) or is_cyclic_shift(sorted_arr, arr) or count_inversions(arr):
        print(True)
    else:
        print(False)
