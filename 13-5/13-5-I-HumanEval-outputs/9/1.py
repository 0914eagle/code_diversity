
from typing import List

def count_nums(arr: List[int]) -> int:
    
    count = 0
    for num in arr:
        if sum(int(digit) for digit in str(num)) > 0:
            count += 1
    return count

