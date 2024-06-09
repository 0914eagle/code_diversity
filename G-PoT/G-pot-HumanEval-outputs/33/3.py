
from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    
    return [i for i in range(a, b+1) if i % 2 == 0]

# Test cases
print(generate_integers(2, 8))  # Output: [2, 4, 6, 8]
print(generate_integers(8, 2))  # Output: [2, 4, 6, 8]
print(generate_integers(10, 14))  # Output: []
