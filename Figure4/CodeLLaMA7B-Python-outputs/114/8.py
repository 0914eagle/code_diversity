def minSubArraySum(nums):
    
    # O(n)
    # O(1)
    if not nums:
        return 0
    min_sum = nums[0]
    cur_sum = nums[0]
    for i in range(1, len(nums)):
        cur_sum = min(cur_sum + nums[i], nums[i])
        min_sum = min(min_sum, cur_sum)
    return min_sum


