
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
                num, digit = divmod(num, 10)
                if digit > 0:
                    count += 1
    return count

