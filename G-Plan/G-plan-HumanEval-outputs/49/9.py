
from typing import List

def find_median_sorted(nums: List[int]) -> float:
    n = len(nums)
    nums.sort()
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]

def median(l: List[int]) -> float:
    return find_median_sorted(l)

if __name__ == "__main__":
    l = list(map(int, input().split()))
    print(median(l))
