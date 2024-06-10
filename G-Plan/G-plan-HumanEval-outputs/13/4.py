
from typing import List

def minSubArraySum(nums: List[int]) -> int:
    def min_sub_array_sum(nums: List[int]) -> int:
        start = 0
        end = 0
        min_sum = float('inf')
        current_sum = 0

        while end < len(nums):
            current_sum += nums[end]
            while current_sum < 0:
                current_sum -= nums[start]
                start += 1
            min_sum = min(min_sum, current_sum)
            end += 1

        return min_sum

    return min_sub_array_sum(nums)

if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(minSubArraySum(nums))
