
from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    
    if a > b:
        a, b = b, a
    even_digits = []
    for num in range(a, b+1):
        if str(num)[-1] in '02468':
            even_digits.append(num)
    return even_digits

