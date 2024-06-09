
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
        if current_sum > 0:
            current_sum = 0
    
    return min_sum

