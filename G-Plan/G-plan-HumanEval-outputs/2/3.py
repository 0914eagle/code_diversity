
from typing import List

def is_sorted(arr: List[int]) -> bool:
    return arr == sorted(arr)

def using_sorting(arr: List[int]) -> bool:
    return is_sorted(arr)

def using_observation(arr: List[int]) -> bool:
    return arr.index(max(arr)) == len(arr) - 1

def using_cyclic_shifts(arr: List[int]) -> bool:
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i:] + arr[:i] == sorted_arr:
            return True
    return False

def count_inversions(arr: List[int]) -> bool:
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions % 2 == 0

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    print(using_sorting(arr))
    print(using_observation(arr))
    print(using_cyclic_shifts(arr))
    print(count_inversions(arr))
