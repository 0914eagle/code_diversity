
from typing import List

def median(l: List[int]) -> float:
    def find_median(sorted_list):
        n = len(sorted_list)
        if n % 2 == 0:
            return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        else:
            return sorted_list[n // 2]

    sorted_list = sorted(l)
    result = find_median(sorted_list)
    return result

# Test the function with example inputs
if __name__ == "__main__":
    input_list = input().strip().split()
    input_list = [int(x) for x in input_list]
    print(median(input_list))
