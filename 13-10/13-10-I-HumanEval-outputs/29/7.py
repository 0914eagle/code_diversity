
from typing import List

def minSubArraySum(nums: List[int]) -> int:
    
    # Initialize the minimum sum to the first element of the array
    min_sum = nums[0]
    # Iterate over the rest of the elements
    for i in range(1, len(nums)):
        # If the current element is less than the minimum sum, update the minimum sum
        if nums[i] < min_sum:
            min_sum = nums[i]
    return min_sum

