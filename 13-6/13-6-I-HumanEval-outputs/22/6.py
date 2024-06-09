
from typing import List

def solution(lst: List[int]) -> int:
    
    if len(lst) == 0:
        return 0
    sum_of_odd_even_positions = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            sum_of_odd_even_positions += lst[i]
    return sum_of_odd_even_positions

