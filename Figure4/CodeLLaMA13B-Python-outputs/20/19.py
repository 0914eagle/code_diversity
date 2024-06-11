from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    numbers.sort()
    closest_numbers = numbers[0], numbers[1]
    min_distance = abs(closest_numbers[0] - closest_numbers[1])
    for i in range(1, len(numbers) - 1):
        distance = abs(numbers[i] - numbers[i + 1])
        if distance < min_distance:
            min_distance = distance
            closest_numbers = numbers[i], numbers[i + 1]
    return closest_numbers


if __