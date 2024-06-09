
from typing import List

def count_up_to(n: int) -> List[int]:
    
    prime_numbers = []
    for i in range(2, n):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

def is_prime(n: int) -> bool:
    
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


