
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    # Find the smallest and largest numbers in the list
    smallest = min(numbers)
    largest = max(numbers)

    # Calculate the range of the numbers
    range_ = largest - smallest

    # Create a new list to store the rescaled numbers
    rescaled_numbers = []

    # Loop through the original list and rescale each number
    for number in numbers:
        # Calculate the rescaled number
        rescaled_number = (number - smallest) / range_

        # Add the rescaled number to the new list
        rescaled_numbers.append(rescaled_number)

    return rescaled_numbers

