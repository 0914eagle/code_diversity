
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    # sort the list in ascending order
    numbers.sort()
    # initialize the closest distance and the indices of the closest numbers
    closest_distance = float('inf')
    closest_indices = (0, 0)
    # loop through the list and compare the distance between each pair of numbers
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < closest_distance:
                closest_distance = distance
                closest_indices = (i, j)
    # return the closest numbers in order
    return (numbers[closest_indices[0]], numbers[closest_indices[1]])

