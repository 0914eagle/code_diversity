
from typing import List

def count_nums(arr: List[int]) -> int:
    
    count = 0
    for num in arr:
        if num < 0:
            count += 1
        else:
            count += sum(int(digit) for digit in str(num))
    return count

