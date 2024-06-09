
from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    
    return sorted(nums, key=lambda x: (sum(int(i) for i in str(abs(x))), x))

