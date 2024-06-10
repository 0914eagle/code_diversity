
from typing import List

def median(l: List[int]) -> float:
    def find_median(sorted_list: List[int]) -> float:
        n = len(sorted_list)
        if n % 2 == 0:
            return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        else:
            return sorted_list[n // 2]

    sorted_l = sorted(l)
    result = find_median(sorted_l)
    return result

# Test cases
if __name__ == "__main__":
    input_list = input().strip().split()
    input_list = [int(x) for x in input_list]
    print(median(input_list))
