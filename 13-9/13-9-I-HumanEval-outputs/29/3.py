
from typing import List

def get_odd_collatz(n: int) -> List[int]:
    
    if n < 1:
        raise ValueError("n must be a positive integer")

    odd_collatz = []
    curr_num = n
    while curr_num > 1:
        if curr_num % 2 == 0:
            curr_num //= 2
        else:
            curr_num = curr_num * 3 + 1
        if curr_num % 2 == 1:
            odd_collatz.append(curr_num)

    return sorted(odd_collatz)

