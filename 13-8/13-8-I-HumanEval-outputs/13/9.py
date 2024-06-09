
from typing import List

def count_nums(arr: List[int]) -> int:
    
    count = 0
    for num in arr:
        if num < 0:
            count += 1
        else:
            count += len([digit for digit in str(num) if digit != '0'])
    return count

