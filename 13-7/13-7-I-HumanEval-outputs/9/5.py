
from typing import List

def search(lst: List[int]) -> int:
    
    # Your code here
    freq = {}
    for i in lst:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    for i in sorted(freq, reverse=True):
        if freq[i] >= i:
            return i
    return -1

