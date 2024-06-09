
from typing import List

def search(lst: List[int]) -> int:
    
    # Your code here
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    
    for num, count in counts.items():
        if count >= num and num > 0:
            return num
    
    return -1

