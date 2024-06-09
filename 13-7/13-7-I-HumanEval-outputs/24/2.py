
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    unique_list = []
    for num in x:
        if all(digit not in [0, 2, 4, 6, 8] for digit in str(num)):
            unique_list.append(num)
    return sorted(unique_list)

