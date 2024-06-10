
from typing import List

def median(l: List[int]) -> float:
    def find_median_odd(sorted_list: List[int]) -> float:
        return sorted_list[len(sorted_list) // 2]

    def find_median_even(sorted_list: List[int]) -> float:
        mid = len(sorted_list) // 2
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

    def sort_list(input_list: List[int]) -> List[int]:
        return sorted(input_list)

    sorted_list = sort_list(l)
    if len(sorted_list) % 2 == 0:
        return find_median_even(sorted_list)
    else:
        return find_median_odd(sorted_list)

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    print(median(input_list))
