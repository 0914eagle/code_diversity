
from typing import List

def search(lst: List[int]) -> int:
    
    # Your code here
    freq = {}
    for num in lst:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    for num, count in freq.items():
        if count >= num:
            return num
    
    return -1

