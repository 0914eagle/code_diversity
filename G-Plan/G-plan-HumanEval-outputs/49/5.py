
from typing import List

def median(l: List[int]) -> float:
    def find_median_odd(sorted_list):
        return sorted_list[len(sorted_list) // 2]

    def find_median_even(sorted_list):
        mid = len(sorted_list) // 2
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

    def calculate_median(input_list):
        sorted_list = sorted(input_list)
        if len(sorted_list) % 2 == 0:
            return find_median_even(sorted_list)
        else:
            return find_median_odd(sorted_list)

    if __name__ == "__main__":
        input_list = list(map(int, input().strip().split()))
        print(calculate_median(input_list))

