
from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    
    # Calculate the sum of the digits of each number
    digit_sums = [sum(int(digit) for digit in str(num)) for num in nums]
    # Zip the original list with the digit sums
    nums_with_digit_sums = list(zip(nums, digit_sums))
    # Sort the list based on the digit sums
    nums_with_digit_sums.sort(key=lambda x: x[1])
    # Return the original list of numbers
    return [num for num, _ in nums_with_digit_sums]

