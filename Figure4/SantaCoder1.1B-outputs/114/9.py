def minSubArraySum(nums):
    
    if not nums:
        return 0
    min_sum = nums[0]
    for i in range(1, len(nums)):
        min_sum = min(min_sum + nums[i], nums[i])
    return min_sum


