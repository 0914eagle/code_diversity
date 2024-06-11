from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find closest elements")

    min_diff = float("inf")
    min_diff_index = 0
    for i in range(len(numbers)):
        diff = abs(numbers[i] - numbers[min_diff_index])
        if diff < min_diff:
            min_diff = diff
            min_diff_index = i

    return numbers[min_diff_index], numbers[min_diff_index + 1]


