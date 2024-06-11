def minSubArraySum(nums):
    
    # 1. Brute Force
    #   - O(n^2)
    #   - Time Limit Exceeded
    # min_sum = float('inf')
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         min_sum = min(min_sum, sum(nums[i:j+1]))
    # return min_sum

    # 2. Two Pointers
    #   - O(n)
    #   - Time Limit Exceeded
    # min_sum = float('inf')
    # left = 0
    # right = 0
    # while right < len(nums):
    #     min_sum = min(min_sum, sum(nums[left:right+1]))
    #     right += 1
    #     if right == len(nums) or nums[left] != nums[right]:
    #         left += 1
    # return min_sum

    # 3. Two Pointers
    #   - O(n)
    #   - 120 ms
    min_sum = float('inf')
    left = 0
    right = 0
    cur_sum = 0
    while right < len(nums):
        cur_sum += nums[right]
        min_sum = min(min_sum, cur_sum)
        right += 1
        if cur_sum < 0:
            cur_sum = 0
            left = right
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
