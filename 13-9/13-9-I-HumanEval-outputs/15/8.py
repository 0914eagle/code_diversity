
from typing import List

def count_nums(arr: List[int]) -> int:
    
    count = 0
    for num in arr:
        if num > 0:
            count += 1
        elif num < 0:
            count += 1 if sum(str(num)) > 0 else 0
    return count

