
from typing import List

def specialFilter(nums: List[int]) -> int:
    
    count = 0
    for num in nums:
        if num > 10 and num % 10 == num // 10 % 10:
            count += 1
    return count

