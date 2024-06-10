
from typing import List

def minSubArraySum(nums: List[int]) -> int:
    
    # Initialize variables
    min_sum = float('inf')
    curr_sum = 0
    
    # Iterate through the array
    for i in range(len(nums)):
        # Add the current element to the current sum
        curr_sum += nums[i]
        
        # If the current sum is less than the minimum sum, update the minimum sum
        if curr_sum < min_sum:
            min_sum = curr_sum
        
        # If the current sum is greater than zero, set it to zero
        # This is done to avoid taking into account any negative numbers
        if curr_sum > 0:
            curr_sum = 0
    
    return min_sum

