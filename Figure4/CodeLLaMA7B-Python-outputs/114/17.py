def minSubArraySum(nums):
    
    # 1. Brute Force
    #   - O(n^2)
    #   - O(1)
    # min_sum = float('inf')
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         min_sum = min(min_sum, sum(nums[i:j+1]))
    # return min_sum

    # 2. Two Pointers
    #   - O(n)
    #   - O(1)
    min_sum = float('inf')
    left = 0
    right = 0
    sum_ = 0
    while right < len(nums):
        sum_ += nums[right]
        while sum_ < min_sum:
            min_sum = sum_
            left = right
        right += 1
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
