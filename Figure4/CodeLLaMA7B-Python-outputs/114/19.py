def minSubArraySum(nums):
    
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(nums[0], nums[1])
    if len(nums) == 3:
        return min(nums[0], nums[1], nums[2])

    min_sum = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        min_sum = min(min_sum, nums[i] + nums[i + 1] + nums[i + 2])
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
