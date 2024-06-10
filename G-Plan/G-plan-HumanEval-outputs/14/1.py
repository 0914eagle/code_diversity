
from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    def find_pairs_using_set(nums):
        seen = set()
        for num in nums:
            if -num in seen:
                return True
            seen.add(num)
        return False

    def find_pairs_using_sorting(nums):
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == 0:
                return True
            elif total > 0:
                right -= 1
            else:
                left += 1
        return False

    if len(l) < 2:
        return False

    return find_pairs_using_set(l)  # Choose the desired approach here

# Read input
input_list = list(map(int, input().split()))

# Output
print(pairs_sum_to_zero(input_list))
