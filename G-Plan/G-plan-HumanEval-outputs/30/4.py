
from typing import List

def is_monotonic_increasing(l: List[int]) -> bool:
    i = 0
    while i < len(l) - 1:
        if l[i] > l[i + 1]:
            return False
        i += 1
    return True

def is_monotonic_decreasing(l: List[int]) -> bool:
    i = 0
    while i < len(l) - 1:
        if l[i] < l[i + 1]:
            return False
        i += 1
    return True

def monotonic(l: List[int]) -> bool:
    return is_monotonic_increasing(l) or is_monotonic_decreasing(l)

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    print(monotonic(input_list))
