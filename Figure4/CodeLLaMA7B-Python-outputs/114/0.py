def minSubArraySum(nums):
    
    # if len(nums) == 1:
    #     return nums[0]
    # else:
    #     return min(minSubArraySum(nums[1:]), nums[0] + minSubArraySum(nums[1:]))

    min_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = min(current_sum + nums[i], nums[i])
        min_sum = min(current_sum, min_sum)
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
