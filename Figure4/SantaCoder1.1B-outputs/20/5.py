from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest pair of numbers")
    if len(numbers) == 2:
        return numbers
    if len(numbers) == 3:
        return min(numbers), max(numbers)
    if len(numbers) == 4:
        return min(numbers), max(numbers), min(numbers), max(numbers)
    if len(numbers) == 5:
        return min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers)
    if len(numbers) == 6:
        return min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers)
    if len(numbers) == 7:
        return min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers)
    if len(numbers) == 8:
        return min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers)
    if len(numbers) == 9:
        return min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers)
    if len(numbers) == 10:
        return min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers)
    if len(numbers) == 11:
        return min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers), min(numbers), max(numbers)
    if