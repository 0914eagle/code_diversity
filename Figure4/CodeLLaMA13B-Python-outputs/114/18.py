def minSubArraySum(nums):
    
    if not nums:
        return 0
    min_sum = nums[0]
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        if total < min_sum:
            min_sum = total
        if total > 0:
            total = 0
    return min_sum


if __name__ == "