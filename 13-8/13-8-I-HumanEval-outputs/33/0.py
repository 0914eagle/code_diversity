
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    # find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # calculate the scaling factor
    scaling_factor = (max_value - min_value) / (len(numbers) - 1)

    # apply the scaling factor to each number
    rescaled_numbers = [(number - min_value) / scaling_factor for number in numbers]

    return rescaled_numbers

