
from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    
    # Initialize an empty list to store the even digits
    even_digits = []

    # Iterate from a to b
    for num in range(a, b + 1):
        # Check if the current number is even
        if num % 2 == 0:
            # Add the even number to the list
            even_digits.append(num)

    # Return the list of even digits
    return even_digits

