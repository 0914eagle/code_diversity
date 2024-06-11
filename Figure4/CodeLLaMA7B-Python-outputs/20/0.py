from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    min_diff = numbers[1] - numbers[0]
    min_diff_indexes = [0, 1]
    for i in range(2, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff < min_diff:
            min_diff = diff
            min_diff_indexes = [i - 1, i]
    return numbers[min_diff_indexes[0]], numbers[min_diff_indexes[1]]


if __