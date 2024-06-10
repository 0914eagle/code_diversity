
from typing import List

def is_monotonic_increasing(l: List[int]) -> bool:
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            return False
    return True

def is_monotonic_decreasing(l: List[int]) -> bool:
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            return False
    return True

def monotonic(l: List[int]) -> bool:
    return is_monotonic_increasing(l) or is_monotonic_decreasing(l)

if __name__ == "__main__":
    l = list(map(int, input().split()))
    print(monotonic(l))
