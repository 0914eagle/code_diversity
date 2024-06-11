from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest pair")
    closest_numbers = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < abs(numbers[i] - closest_numbers[0]):
                closest_numbers = [numbers[i], numbers[j]]
    return closest_numbers


