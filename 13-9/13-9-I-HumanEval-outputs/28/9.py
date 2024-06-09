
from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    
    # Check if a and b are positive integers
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive integers")

    # Initialize an empty list to store the even digits
    even_digits = []

    # Loop through the range of a to b (inclusive)
    for num in range(a, b + 1):
        # Check if the current number is even
        if num % 2 == 0:
            # Add the even number to the list
            even_digits.append(num)

    # Return the list of even digits
    return even_digits

