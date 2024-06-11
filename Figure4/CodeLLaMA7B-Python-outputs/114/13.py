def minSubArraySum(nums):
    
    # if len(nums) == 1:
    #     return nums[0]
    # else:
    #     return min(minSubArraySum(nums[:-1]), nums[-1] + minSubArraySum(nums[:-2]))
    # O(n) time, O(n) space

    # O(1) time, O(1) space
    min_sum = float('inf')
    cur_sum = 0
    for num in nums:
        cur_sum += num
        min_sum = min(min_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return min_sum


