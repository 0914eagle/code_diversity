
from typing import List

def count_nums(arr: List[int]) -> int:
    
    count = 0
    for num in arr:
        if num < 0:
            num = -num
        count += 1 if sum(int(digit) for digit in str(num)) > 0 else 0
    return count

