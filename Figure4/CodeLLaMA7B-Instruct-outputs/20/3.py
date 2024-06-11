
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    closest_pair = (numbers[0], numbers[1])

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[j] - numbers[i]) < abs(closest_pair[1] - closest_pair[0]):
                closest_pair = (numbers[i], numbers[j])

    return closest_pair

