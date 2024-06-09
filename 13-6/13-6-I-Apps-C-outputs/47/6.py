
import math

def solve(k):
    def is_perfect(nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] ^ nums[j]) not in nums:
                    return False
        return True

    nums = list(range(k+1))
    return sum(1 for i in range(len(nums)) if is_perfect(nums[:i+1])) % (10**9+7)

