
from typing import List

def minSubArraySum(nums: List[int]) -> int:
    
    # Initialize variables
    min_sum = float('inf')
    window_sum = 0
    start = 0
    
    # Iterate through the array
    for end in range(len(nums)):
        # Add the current element to the window sum
        window_sum += nums[end]
        
        # If the window sum is less than the minimum sum, update the minimum sum
        if window_sum < min_sum:
            min_sum = window_sum
        
        # If the window sum is greater than the minimum sum, slide the window
        if window_sum - nums[start] > min_sum:
            min_sum = window_sum - nums[start]
            start += 1
    
    return min_sum

