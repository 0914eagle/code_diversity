
from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    
    return all(i < t for i in l)

