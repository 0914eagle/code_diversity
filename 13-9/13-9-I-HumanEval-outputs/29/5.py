
from typing import List

def get_odd_collatz(n: int) -> List[int]:
    
    # Initialize an empty list to store the odd numbers
    odd_numbers = []

    # Initialize a variable to store the current number
    current_number = n

    # Iterate until the current number is 1
    while current_number != 1:
        # If the current number is odd, add it to the list of odd numbers
        if current_number % 2 == 1:
            odd_numbers.append(current_number)

        # Update the current number based on the Collatz sequence
        if current_number % 2 == 0:
            current_number = current_number // 2
        else:
            current_number = 3 * current_number + 1

    # Add 1 to the list of odd numbers, since the Collatz sequence starts with 1
    odd_numbers.append(1)

    # Return the sorted list of odd numbers
    return sorted(odd_numbers)

