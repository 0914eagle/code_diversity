
from typing import List

def minSubArraySum(nums: List[int]) -> int:
    
    # Initialize a variable to store the minimum sum
    min_sum = float('inf')
    # Initialize a variable to store the current sum
    current_sum = 0
    # Iterate through the array
    for num in nums:
        # Add the current number to the current sum
        current_sum += num
        # If the current sum is less than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
        # If the current sum is greater than zero, set it to zero
        if current_sum > 0:
            current_sum = 0
    # Return the minimum sum
    return min_sum

