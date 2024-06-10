
from typing import List

def find_median(lst: List[int]) -> float:
    n = len(lst)
    lst.sort()
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = find_median(input_list)
    print(result)
