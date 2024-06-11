def minSubArraySum(nums):
    
    min_sum = nums[0]
    sum = 0
    for num in nums:
        sum += num
        min_sum = min(min_sum, sum)
        if sum < 0:
            sum = 0
    return min_sum


