def minSubArraySum(nums):
    
    if not nums:
        return 0
    min_sum = sum(nums)
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > 0:
            current_sum = 0
    return min_sum


if __name__ == "