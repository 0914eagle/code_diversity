
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    # Your code here
    res = []
    for i in x:
        if all(int(j) % 2 != 0 for j in str(i)):
            res.append(i)
    return sorted(res)

