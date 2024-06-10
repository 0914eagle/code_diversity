
from typing import List

def monotonic(l: List[int]) -> bool:
    
    dir_ = 1 if l[1] >= l[0] else -1
    for i in range(1, len(l)):
        if l[i] * dir_ < l[i-1] * dir_:
            return False
    return True

