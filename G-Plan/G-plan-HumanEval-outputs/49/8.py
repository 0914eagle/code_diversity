
from typing import List

def find_median(lst: List[int]) -> float:
    n = len(lst)
    lst.sort()
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

if __name__ == "__main__":
    l = list(map(int, input().split()))
    result = find_median(l)
    print(result)
