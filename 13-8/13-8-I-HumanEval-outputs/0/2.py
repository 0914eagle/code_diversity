
from typing import List

def specialFilter(nums: List[int]) -> int:
    
    count = 0
    for num in nums:
        if num > 10 and (num % 10) % 2 == 1 and (num // 10) % 2 == 1:
            count += 1
    return count

