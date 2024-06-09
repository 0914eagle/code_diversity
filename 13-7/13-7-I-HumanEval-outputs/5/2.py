
from typing import List

def minSubArraySum(nums: List[int]) -> int:
    
    # Initialize the minimum sum to a large value
    min_sum = float('inf')
    # Iterate over the sub-arrays of nums
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            # Calculate the sum of the current sub-array
            current_sum = sum(nums[i:j+1])
            # Update the minimum sum if necessary
            min_sum = min(min_sum, current_sum)
    # Return the minimum sum
    return min_sum

