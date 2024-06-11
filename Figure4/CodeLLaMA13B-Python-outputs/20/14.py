from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    numbers.sort()
    min_distance = float('inf')
    min_distance_pair = (float('inf'), float('inf'))
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < min_distance:
            min_distance = numbers[i + 1] - numbers[i]
            min_distance_pair = (numbers[i], numbers[i + 1])
    return min_distance_pair


if __name__