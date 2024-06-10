
from typing import List

def calculate_digit_sum(num: int) -> int:
    return sum(int(digit) for digit in str(abs(num)))

def order_by_points(nums: List[int]) -> List[int]:
    def custom_comparison(x: int, y: int) -> int:
        if calculate_digit_sum(x) == calculate_digit_sum(y):
            return nums.index(x) - nums.index(y)
        return calculate_digit_sum(x) - calculate_digit_sum(y)

    return sorted(nums, key=lambda x: (calculate_digit_sum(x), nums.index(x)))

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = order_by_points(nums)
    print(result)
