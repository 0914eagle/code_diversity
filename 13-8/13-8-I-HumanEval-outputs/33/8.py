
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    # find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # calculate the range of the values
    range_values = max_value - min_value

    # create a new list to store the rescaled values
    rescaled_numbers = []

    # loop through the original list and calculate the rescaled values
    for num in numbers:
        rescaled_num = (num - min_value) / range_values
        rescaled_numbers.append(rescaled_num)

    return rescaled_numbers

