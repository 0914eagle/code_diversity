
from typing import List

def search(lst: List[int]) -> int:
    
    # Your code here
    counts = {}
    for num in lst:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    
    for num in reversed(sorted(counts.keys())):
        if counts[num] >= num:
            return num
    return -1

