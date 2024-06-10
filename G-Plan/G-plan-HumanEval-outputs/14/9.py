
from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    def find_pairs_using_set(nums):
        seen = set()
        for num in nums:
            if -num in seen:
                return True
            seen.add(num)
        return False

    def find_pairs_sorting_pointers(nums):
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == 0:
                return True
            elif current_sum > 0:
                right -= 1
            else:
                left += 1
        return False

    if len(l) < 2:
        return False

    return find_pairs_using_set(l) or find_pairs_sorting_pointers(l)

l = list(map(int, input().split()))
print(pairs_sum_to_zero(l))
