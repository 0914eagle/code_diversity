
from typing import List

def specialFilter(nums: List[int]) -> int:
    
    count = 0
    for num in nums:
        if num > 10 and (num % 10 == 1 or num % 10 == 3 or num % 10 == 5 or num % 10 == 7 or num % 10 == 9) and (num // 10 == 1 or num // 10 == 3 or num // 10 == 5 or num // 10 == 7 or num // 10 == 9):
            count += 1
    return count

