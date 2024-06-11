from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest elements")

    smallest = numbers[0]
    smallest_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
            smallest_index = i

    largest = numbers[0]
    largest_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
            largest_index = i

    return (smallest, largest), (smallest_index, largest_index)


