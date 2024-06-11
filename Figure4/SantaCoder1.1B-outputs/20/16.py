from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest")
    if len(numbers) == 2:
        return numbers
    if numbers[0] > numbers[1]:
        numbers.reverse()
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]:
        return numbers
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]:
        return numbers
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]:
        return numbers
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]:
        return numbers
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]:
        return numbers
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]:
        return numbers
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]:
        return numbers
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]:
        return numbers
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]:
        return numbers
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]:
        return numbers
    if numbers[0] == numbers[1]:
        return numbers
    if numbers[0] == numbers[2]:
        return numbers
    if numbers[1] == numbers[2]: