
from typing import List

def search(lst: List[int]) -> int:
    
    # Your code here
    max_freq = 0
    res = -1
    for i in lst:
        if lst.count(i) >= i and lst.count(i) > max_freq:
            max_freq = lst.count(i)
            res = i
    return res

