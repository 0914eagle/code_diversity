
from typing import List

def is_monotonic_increasing(l: List[int]) -> bool:
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def is_monotonic_decreasing(l: List[int]) -> bool:
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            return False
    return True

def monotonic(l: List[int]) -> bool:
    return is_monotonic_increasing(l) or is_monotonic_decreasing(l)

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    print(monotonic(input_list))
