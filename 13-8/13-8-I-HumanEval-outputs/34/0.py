
from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    
    # Check if a and b are positive
    if a <= 0 or b <= 0:
        return []
    
    # Initialize an empty list to store the even digits
    even_digits = []
    
    # Iterate from a to b (or from b to a if b < a)
    for num in range(a, b+1):
        # Check if the current number is even
        if num % 2 == 0:
            # Add the number to the list
            even_digits.append(num)
    
    # Return the sorted list of even digits
    return sorted(even_digits)

