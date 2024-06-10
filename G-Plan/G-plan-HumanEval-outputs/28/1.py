
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

# Test the function with example cases
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
