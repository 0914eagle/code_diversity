
from typing import List

def count_nums(arr: List[int]) -> int:
    
    count = 0
    for num in arr:
        if num > 0:
            count += 1
        elif num < 0:
            count += 1
            num = -num
            while num > 0:
                count += 1
                num //= 10
    return count
