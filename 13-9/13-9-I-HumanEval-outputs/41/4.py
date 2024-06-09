
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    # Initialize an empty list to store the unique digits
    unique_list = []

    # Iterate through the list of integers
    for num in x:
        # Check if the number has any even digits
        if not any(int(digit) % 2 == 0 for digit in str(num)):
            # If not, add the number to the unique list
            unique_list.append(num)

    # Return the sorted unique list
    return sorted(unique_list)

