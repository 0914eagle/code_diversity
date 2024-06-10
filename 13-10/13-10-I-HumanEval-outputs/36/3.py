
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    # your code here
    res = []
    for i in x:
        flag = False
        while i > 0:
            if i % 10 % 2 == 0:
                flag = True
                break
            i //= 10
        if not flag:
            res.append(i)
    return sorted(res)

