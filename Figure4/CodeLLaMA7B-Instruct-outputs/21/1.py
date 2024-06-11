
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Calculate the range of the values
    range_val = max_val - min_val

    # Create a new list with the rescaled values
    rescaled_list = []
    for num in numbers:
        rescaled_list.append((num - min_val) / range_val)

    return rescaled_list

