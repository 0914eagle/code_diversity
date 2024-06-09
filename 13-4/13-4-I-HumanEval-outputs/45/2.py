
from typing import List

def minSubArraySum(nums: List[int]) -> int:
    
    # Initialize variables
    min_sum = float('inf')
    current_sum = 0
    
    # Iterate through the array
    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum < min_sum:
            min_sum = current_sum
        elif current_sum > 0:
            current_sum = 0
    
    # Check if the entire array needs to be considered
    if min_sum > sum(nums):
        min_sum = sum(nums)
    
    return min_sum

