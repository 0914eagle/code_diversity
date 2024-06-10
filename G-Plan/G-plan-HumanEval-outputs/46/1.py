
from typing import List

def sum_of_digits(num: int) -> int:
    return sum(int(d) for d in str(abs(num)))

def order_by_points(nums: List[int]) -> List[int]:
    def custom_comparison(x):
        return sum_of_digits(x), nums.index(x)
    
    return sorted(nums, key=custom_comparison)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = order_by_points(nums)
    print(result)
