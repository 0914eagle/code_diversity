
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    smallest_diff = float("inf")
    closest_elements = (None, None)

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < smallest_diff:
                smallest_diff = diff
                closest_elements = (numbers[i], numbers[j])

    return closest_elements

