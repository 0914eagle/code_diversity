
from typing import List

def median(l: List[int]) -> float:
    def find_median(sorted_list: List[int]) -> float:
        n = len(sorted_list)
        if n % 2 == 0:
            return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        else:
            return sorted_list[n // 2]

    sorted_list = sorted(l)
    result = find_median(sorted_list)
    return result

l = list(map(int, input().split()))
print(median(l))
