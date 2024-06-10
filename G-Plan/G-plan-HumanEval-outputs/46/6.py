
from typing import List

def calculate_digit_sum(num: int) -> int:
    return sum(int(digit) for digit in str(abs(num)))

def order_by_points(nums: List[int]) -> List[int]:
    def custom_comparison(num1: int, num2: int) -> int:
        sum1 = calculate_digit_sum(num1)
        sum2 = calculate_digit_sum(num2)
        if sum1 == sum2:
            return nums.index(num1) - nums.index(num2)
        return sum1 - sum2

    return sorted(nums, key=lambda x: (calculate_digit_sum(x), nums.index(x)))

if __name__ == "__main__":
    input_nums = list(map(int, input().split()))
    result = order_by_points(input_nums)
    print(result)
