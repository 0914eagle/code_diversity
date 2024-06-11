def minSubArraySum(nums):
    
    min_sum = nums[0]
    total = 0
    for num in nums:
        total += num
        min_sum = min(min_sum, total)
        if total < 0:
            total = 0
    return min_sum


