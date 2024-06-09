
from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    
    even_digits = []

    for num in range(a, b+1):
        if num % 2 == 0:
            even_digits.append(num)

    return even_digits

