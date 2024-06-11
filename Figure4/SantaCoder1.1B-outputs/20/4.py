from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find closest")

    closest_numbers = []
    for number in numbers:
        closest_numbers.append(abs(number - numbers[0]))

    closest_numbers.sort()
    return closest_numbers[0], closest_numbers[-1]


