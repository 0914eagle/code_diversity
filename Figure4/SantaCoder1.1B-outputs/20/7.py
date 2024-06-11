from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest pair")

    closest_pair = (numbers[0], numbers[1])
    for number in numbers[2:]:
        if abs(number - closest_pair[0]) < abs(number - closest_pair[1]):
            closest_pair = (number, closest_pair[1])
        elif abs(number - closest_pair[1]) < abs(number - closest_pair[0]):
            closest_pair = (closest_pair[0], number)

    return closest_pair


