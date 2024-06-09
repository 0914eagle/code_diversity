
from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    
    # Calculate the sum of the digits of each number
    sums = [sum(int(digit) for digit in str(num)) for num in nums]
    # Zip the sums with the original indices
    indices_and_sums = zip(range(len(nums)), sums)
    # Sort the indices based on the sums
    sorted_indices = sorted(indices_and_sums, key=lambda x: x[1])
    # Return the sorted list of numbers based on the original indices
    return [nums[i] for i, _ in sorted_indices]

