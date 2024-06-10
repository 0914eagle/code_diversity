
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    return sorted([i for i in x if all(int(j) % 2 for j in str(i))])

