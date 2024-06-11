from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    numbers.sort()
    min_diff = float('inf')
    min_diff_pair = (float('inf'), float('inf'))
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < min_diff:
            min_diff = abs(numbers[i] - numbers[i + 1])
            min_diff_pair = (numbers[i], numbers[i + 1])
    return min_diff_pair


if