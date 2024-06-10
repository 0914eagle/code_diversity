
from typing import List

def is_sorted(arr: List[int]) -> bool:
    return arr == sorted(arr)

def using_sorting(arr: List[int]) -> bool:
    return is_sorted(arr)

def using_observation(arr: List[int]) -> bool:
    max_index = arr.index(max(arr))
    return max_index == len(arr) - 1

def is_cyclic_shift(arr1: List[int], arr2: List[int]) -> bool:
    n = len(arr1)
    if n != len(arr2):
        return False
    for i in range(n):
        if arr1 == arr2:
            return True
        arr2 = [arr2[-1]] + arr2[:-1]
    return False

def using_cyclic_shifts(arr: List[int]) -> bool:
    sorted_arr = sorted(arr)
    return is_cyclic_shift(arr, sorted_arr)

def count_inversions(arr: List[int]) -> int:
    inversions = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

def using_counting_inversions(arr: List[int]) -> bool:
    return count_inversions(arr) % 2 == 0

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    print(using_sorting(arr))
    print(using_observation(arr))
    print(using_cyclic_shifts(arr))
    print(using_counting_inversions(arr))
