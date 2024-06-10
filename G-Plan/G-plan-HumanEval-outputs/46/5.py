
from typing import List

def sum_of_digits(num: int) -> int:
    return sum(int(d) for d in str(abs(num)))

def order_by_points(nums: List[int]) -> List[int]:
    def custom_comparison(x: int, y: int) -> int:
        sum_x = sum_of_digits(x)
        sum_y = sum_of_digits(y)
        if sum_x == sum_y:
            return nums.index(x) - nums.index(y)
        return sum_x - sum_y

    return sorted(nums, key=sum_of_digits, cmp=custom_comparison)

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = order_by_points(input_list)
    print(result)
