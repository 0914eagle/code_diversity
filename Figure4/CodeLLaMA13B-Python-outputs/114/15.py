def minSubArraySum(nums):
    
    if len(nums) == 0:
        return 0
    min_sum = sum(nums)
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i : j + 1]) < min_sum:
                min_sum = sum(nums[i : j + 1])
    return min_sum


if