def minSubArraySum(nums):
    
    min_sum = nums[0]
    sum_ = 0
    for num in nums:
        sum_ += num
        min_sum = min(min_sum, sum_)
    return min_sum


