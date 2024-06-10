
from typing import List

def is_sorted(arr: List[int]) -> bool:
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def move_one_ball(arr: List[int]) -> bool:
    if not arr:
        return True

    if is_sorted(arr):
        return True

    max_val = max(arr)
    max_idx = arr.index(max_val)

    return max_idx == len(arr) - 1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(move_one_ball(arr))
