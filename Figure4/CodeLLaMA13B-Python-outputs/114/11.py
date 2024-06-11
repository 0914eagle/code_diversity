def minSubArraySum(nums):
    
    min_sum = nums[0]
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > 0:
            current_sum = 0
    return min_sum


if __name__ == "__main__":
    nums = [2, 3,