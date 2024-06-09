
from typing import List

def add(lst: List[int]) -> int:
    
    if not lst:
        raise ValueError("lst must be a non-empty list of integers")

    sum_even = 0
    for i, elem in enumerate(lst):
        if elem % 2 == 0 and i % 2 == 1:
            sum_even += elem

    return sum_even

