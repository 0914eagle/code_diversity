from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest pair")
    closest_number = numbers[0]
    closest_distance = abs(numbers[0] - numbers[1])
    for number in numbers[1:]:
        distance = abs(number - closest_number)
        if distance < closest_distance:
            closest_number = number
            closest_distance = distance
    return closest_number, closest_distance


