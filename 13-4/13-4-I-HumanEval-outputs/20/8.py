
from typing import List

def count_nums(arr: List[int]) -> int:
    
    count = 0
    for num in arr:
        if num > 0:
            count += 1
        elif num < 0:
            count += 1
            num = abs(num)
            while num > 0:
                if num % 10 > 0:
                    count += 1
                num //= 10
    return count

