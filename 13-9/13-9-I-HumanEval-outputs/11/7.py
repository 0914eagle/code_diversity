
from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    
    return sorted(arr, reverse=True)[:k]

