
from typing import List

def sort_third(l: List[int]) -> List[int]:
    
    # your code here
    return sorted([l[i] for i in range(len(l)) if i % 3 == 0]) + [l[i] for i in range(len(l)) if i % 3 != 0]

