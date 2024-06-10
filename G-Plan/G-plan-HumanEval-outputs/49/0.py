
from typing import List

def median(l: List[int]) -> float:
    def find_median(sorted_list: List[int]) -> float:
        n = len(sorted_list)
        if n % 2 == 0:
            return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        else:
            return sorted_list[n // 2]

    def sort_list(l: List[int]) -> List[int]:
        return sorted(l)

    if not l:
        return 0.0

    sorted_list = sort_list(l)
    return find_median(sorted_list)

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = median(input_list)
    print(result)
