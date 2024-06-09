
from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    
    num_str = str(num)
    count_even = 0
    count_odd = 0
    for digit in num_str:
        if int(digit) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd

