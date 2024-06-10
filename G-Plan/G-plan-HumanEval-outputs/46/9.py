
from typing import List

def digit_sum(num: int) -> int:
    return sum(int(digit) for digit in str(abs(num)))

def order_by_points(nums: List[int]) -> List[int]:
    def custom_comparison(x):
        return (digit_sum(x), nums.index(x))

    return sorted(nums, key=custom_comparison)

if __name__ == "__main__":
    input_nums = list(map(int, input().split()))
    result = order_by_points(input_nums)
    print(result)
