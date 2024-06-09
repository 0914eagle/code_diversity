
from typing import List

def count_up_to(n: int) -> List[int]:
    
    if n < 2:
        return []
    prime_numbers = [2]
    for i in range(3, n+1, 2):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers

