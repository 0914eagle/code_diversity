
from typing import List

def minSubArraySum(nums: List[int]) -> int:
    
    # Initialize a variable to store the minimum sum
    min_sum = float('inf')
    
    # Iterate over the array
    for i in range(len(nums)):
        # Initialize a variable to store the sum
        current_sum = 0
        
        # Iterate over the sub-array
        for j in range(i, len(nums)):
            # Add the current element to the sum
            current_sum += nums[j]
            
            # If the sum is less than the minimum sum, update the minimum sum
            if current_sum < min_sum:
                min_sum = current_sum
    
    # Return the minimum sum
    return min_sum

