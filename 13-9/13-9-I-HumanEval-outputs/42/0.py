
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    sorted_numbers = sorted(numbers)
    smallest_distance = abs(sorted_numbers[0] - sorted_numbers[1])
    closest_elements = (sorted_numbers[0], sorted_numbers[1])

    for i in range(1, len(numbers) - 1):
        distance = abs(sorted_numbers[i] - sorted_numbers[i+1])
        if distance < smallest_distance:
            smallest_distance = distance
            closest_elements = (sorted_numbers[i], sorted_numbers[i+1])

    return closest_elements

