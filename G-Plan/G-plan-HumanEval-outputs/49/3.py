
from typing import List

def find_median(nums: List[int]) -> float:
    n = len(nums)
    nums.sort()
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]

if __name__ == "__main__":
    l = list(map(int, input().split()))
    result = find_median(l)
    print(result)
