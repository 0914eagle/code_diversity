
from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    
    return all(x < t for x in l)

