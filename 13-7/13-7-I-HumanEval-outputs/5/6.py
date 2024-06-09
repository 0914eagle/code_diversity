
from typing import List

def minSubArraySum(nums: List[int]) -> int:
    
    # Initialize the minimum sum to a large value
    min_sum = float('inf')
    # Iterate over the array
    for i in range(len(nums)):
        # Calculate the sum of the current sub-array
        current_sum = sum(nums[i:])
        # Update the minimum sum if the current sum is smaller
        if current_sum < min_sum:
            min_sum = current_sum
    return min_sum

