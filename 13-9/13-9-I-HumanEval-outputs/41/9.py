
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    # Initialize an empty list to store the unique digits
    unique_digits_list = []

    # Iterate through the input list
    for num in x:
        # Check if the number has any even digit
        if not any(str(num).endswith(digit) for digit in ["0", "2", "4", "6", "8"]):
            # If not, add the number to the unique digits list
            unique_digits_list.append(num)

    # Return the sorted unique digits list
    return sorted(unique_digits_list)

