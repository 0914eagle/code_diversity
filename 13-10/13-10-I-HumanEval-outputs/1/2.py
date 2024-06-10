
from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    
    # Sort the list by the sum of the digits
    nums.sort(key=lambda x: sum(int(d) for d in str(abs(x))))
    # Sort again if there are items with the same sum of digits
    nums.sort(key=lambda x: x)
    return nums

