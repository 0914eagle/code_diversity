def minSubArraySum(nums):
    
    # init
    min_sum = float('inf')
    curr_sum = 0
    # loop through nums
    for i in range(len(nums)):
        curr_sum += nums[i]
        min_sum = min(min_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
