def minSubArraySum(nums):
    
    min_sum = nums[0]
    sum_ = 0
    for num in nums:
        sum_ += num
        if sum_ < min_sum:
            min_sum = sum_
        if sum_ > 0:
            sum_ = 0
    return min_sum


