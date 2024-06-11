def minSubArraySum(nums):
    
    # O(n) time, O(1) space
    min_sum = float('inf')
    min_sum_so_far = float('inf')
    for num in nums:
        min_sum_so_far = min(min_sum_so_far + num, num)
        min_sum = min(min_sum, min_sum_so_far)
    return min_sum


