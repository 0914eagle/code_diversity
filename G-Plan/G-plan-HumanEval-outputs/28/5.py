
from typing import List

def median(l: List[int]) -> float:
    def find_median(sorted_list: List[int]) -> float:
        n = len(sorted_list)
        if n % 2 == 1:
            return sorted_list[n // 2]
        else:
            mid_right = n // 2
            mid_left = mid_right - 1
            return (sorted_list[mid_left] + sorted_list[mid_right]) / 2

    sorted_l = sorted(l)
    result = find_median(sorted_l)
    return result

# Test the function with example cases
if __name__ == "__main__":
    input_list = input().strip().split()
    input_list = [int(num) for num in input_list]
    print(median(input_list))
