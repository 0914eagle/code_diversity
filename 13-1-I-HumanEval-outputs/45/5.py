
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    unique_list = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            unique_list.append(num)
    return sorted(unique_list)

