
from typing import List

def find_median_odd(sorted_list: List[int]) -> float:
    return sorted_list[len(sorted_list) // 2]

def find_median_even(sorted_list: List[int]) -> float:
    mid = len(sorted_list) // 2
    return (sorted_list[mid - 1] + sorted_list[mid]) / 2

def median(l: List[int]) -> float:
    sorted_list = sorted(l)
    if len(sorted_list) % 2 == 1:
        return find_median_odd(sorted_list)
    else:
        return find_median_even(sorted_list)

if __name__ == "__main__":
    l = list(map(int, input().split()))
    print(median(l))
