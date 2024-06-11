def minSubArraySum(nums):
    
    # O(n) time | O(1) space
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return min_sum if min_sum != float('inf') else 0


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
