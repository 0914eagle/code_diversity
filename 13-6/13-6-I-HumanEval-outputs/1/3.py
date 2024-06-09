
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    sorted_numbers = sorted(numbers)
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    closest_distance = abs(closest_pair[0] - closest_pair[1])

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < closest_distance:
                closest_distance = distance
                closest_pair = (numbers[i], numbers[j])

    return closest_pair

