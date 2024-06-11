def minSubArraySum(nums):
    
    min_sum = nums[0]
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum < min_sum:
            min_sum = sum
        if sum > 0:
            sum = 0
    return min_sum


