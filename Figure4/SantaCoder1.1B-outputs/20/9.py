from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest pair")
    closest_pair = None
    closest_distance = None
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if closest_distance is None or distance < closest_distance:
                closest_distance = distance
                closest_pair = numbers[i], numbers[j]
    return closest_pair


