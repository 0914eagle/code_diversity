def minSubArraySum(nums):
    
    # O(n)
    # O(1)
    min_sum = float('inf')
    cur_sum = 0
    for num in nums:
        cur_sum += num
        min_sum = min(min_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return min_sum


