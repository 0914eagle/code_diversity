from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")

    min_diff = float("inf")
    min_diff_numbers = (float("inf"), float("inf"))

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                min_diff_numbers = (numbers[i], numbers[j])

    return min_diff_numbers


if __