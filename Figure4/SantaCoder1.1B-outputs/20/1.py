from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest")
    sorted_numbers = sorted(numbers)
    closest_number = sorted_numbers[0]
    closest_index = 0
    for index, number in enumerate(sorted_numbers):
        if abs(number - closest_number) < abs(number - numbers[closest_index]):
            closest_number = number
            closest_index = index
    return closest_number, numbers[closest_index]


