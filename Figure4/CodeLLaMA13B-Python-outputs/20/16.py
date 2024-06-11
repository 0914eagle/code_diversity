from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    numbers.sort()
    min_diff = abs(numbers[0] - numbers[1])
    min_diff_pair = (numbers[0], numbers[1])
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < min_diff:
            min_diff = diff
            min_diff_pair = (numbers[i], numbers[i + 1])
    return min_diff_pair


if __