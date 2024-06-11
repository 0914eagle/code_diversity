from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest element")

    # Sort the numbers
    numbers.sort()

    # Find the two numbers that are closest to each other
    closest_numbers = []
    for i in range(len(numbers) - 1):
        closest_numbers.append(numbers[i + 1] - numbers[i])

    # Return the two numbers that are closest to each other
    return min(closest_numbers), max(closest_numbers)


