
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    # Initialize an empty list to store the results
    result = []

    # Iterate through the input list
    for num in x:
        # Check if the number has any even digit
        if not any(digit % 2 == 0 for digit in str(num)):
            # If not, add the number to the result list
            result.append(num)

    # Return the sorted result list
    return sorted(result)

