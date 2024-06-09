
from typing import List

def get_odd_collatz(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    odd_numbers = []
    current_number = n
    while current_number != 1:
        if current_number % 2 == 0:
            current_number = current_number // 2
        else:
            current_number = 3 * current_number + 1
        
        if current_number % 2 == 1:
            odd_numbers.append(current_number)
    
    return sorted(odd_numbers)

