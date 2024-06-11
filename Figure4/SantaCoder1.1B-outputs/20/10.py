from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest elements")
    closest_numbers = []
    for number in numbers:
        closest_numbers.append(find_closest_number(number, numbers))
    return min(closest_numbers), max(closest_numbers)


