
from typing import List

def get_odd_collatz(n: int) -> List[int]:
    
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    odd_numbers = []
    current_number = n
    while current_number != 1:
        if current_number % 2 == 1:
            odd_numbers.append(current_number)
        current_number = collatz_sequence(current_number)
    
    return sorted(odd_numbers)

def collatz_sequence(n: int) -> int:
    
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

